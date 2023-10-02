import React, { useState, useEffect, useRef } from 'react';
import { StyleSheet, Text, View, Image } from 'react-native';
import { Camera, CameraType } from 'expo-camera';
import * as MediaLibrary from 'expo-media-library';
import * as FileSystem from 'expo-file-system'; // Adicionado
import Button from './Button';

export default function App() {

  const [hasCameraPermission, setHasCameraPermission] = useState(null);
  const [image, setImage] = useState(null);
  const [type, setType] = useState(Camera.Constants.Type.back);
  const [flash, setFlash] = useState(Camera.Constants.FlashMode.off);
  const [processedData, setProcessedData] = useState(null);
  const [isImageTaken, setIsImageTaken] = useState(false);
  const cameraRef = useRef(null);

  useEffect(() => {
    (async () => {
      MediaLibrary.requestPermissionsAsync();
      const cameraStatus = await Camera.requestCameraPermissionsAsync();
      setHasCameraPermission(cameraStatus.status === 'granted');
    })();
  }, [])

  const takePicture = async () => {
    if (cameraRef.current) {
      try {
        const data = await cameraRef.current.takePictureAsync();
        console.log(data);
        setImage(data.uri);
        setIsImageTaken(true);

        const byteArray = await FileSystem.readAsStringAsync(data.uri, {
          encoding: FileSystem.EncodingType.Base64,
        });
        setProcessedData(byteArray);
      } catch (e) {
        console.error(e);
      }
    }
  };


  const saveImage = async () => {
    if (isImageTaken) {
      const formData = new FormData();
      formData.append('file', {
        uri: image,
        name: 'imagem.jpg',
        type: 'image/jpg',
      });

      try {
        const response = await fetch('http://172.18.0.1:5000/home', {
          method: 'POST',
          body: formData,
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });

        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        console.log(data);

        if (data && data.Txts) {
          console.log('Textos Identificados:');
          data.Txts.forEach((texto, index) => {
            console.log(`${index + 1}. ${texto}`);
          });
        }

        setProcessedData(data);
        console.log(processedData);
      } catch (error) {
        console.error('Erro ao enviar a imagem:', error);
      }

      setImage(null);
      setIsImageTaken(false);
    }
  }


  if (hasCameraPermission === false) {
    return <Text> No access to camera</Text>
  }

  return (
    <View style={styles.container}>
      {!image ?
        <Camera
          style={styles.camera}
          type={type}
          flashMode={flash}
          ref={cameraRef}
        >
          <View style={{
            flexDirection: 'row',
            justifyContent: 'space-between',
            padding: 30,
          }}>
            <Button icon={'retweet'} onPress={() => {
              setType(type === CameraType.back ? CameraType.front : CameraType.back)
            }} />
            <Button icon={'flash'}
              color={flash === Camera.Constants.FlashMode.off ? 'gray' : '#f1f1f1'}
              onPress={() => {
                setFlash(flash === Camera.Constants.FlashMode.off
                  ? Camera.Constants.FlashMode.on
                  : Camera.Constants.FlashMode.off
                )
              }} />
          </View>
        </Camera>
        :
        <Image source={{ uri: image }} style={styles.camera} />
      }
      <View>
        {image ?
          <View style={{
            flexDirection: 'row',
            justifyContent: 'space-between',
            paddingHorizontal: 50
          }}>
            <Button title={"Re-take"} icon="retweet" onPress={() => setImage(null)} />
            <Button title={"Save"} icon="check" onPress={saveImage} />
          </View>
          :
          <Button title={'Take a picture'} icon="camera" onPress={takePicture} />
        }
      </View>
  
      {/* Exibir os textos processados */}
      {processedData && processedData.Txts && (
        <View style={{ marginTop: 20 }}>
          <Text style={{ fontSize: 20, fontWeight: 'bold' }}>Textos Processados:</Text>
          {processedData.Txts.map((texto, index) => (
            <Text key={index} style={{ fontSize: 16 }}>{texto}</Text>
          ))}
        </View>
      )}
    </View>
  );
  
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#000',
    justifyContent: 'center',
    paddingBottom: 20
  },

  camera: {
    flex: 1,
    borderRadius: 20,
  },
});
