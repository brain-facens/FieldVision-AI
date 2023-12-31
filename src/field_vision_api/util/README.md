<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<html><head><title>Python: module utils</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head><body bgcolor="#f0f0f8">

<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="heading">
<tr bgcolor="#7799ee">
<td valign=bottom>&nbsp;<br>
<font color="#ffffff" face="helvetica, arial">&nbsp;<br><big><big><strong>utils</strong></big></big></font></td
><td align=right valign=bottom
><font color="#ffffff" face="helvetica, arial"><a href=".">index</a><br><a href="file:/home/nata-brain/Documents/projects/OCR-notas/python_scripts/utils.py">/home/nata-brain/Documents/projects/OCR-notas/python_scripts/utils.py</a></font></td></tr></table>
    <p><tt>Developed&nbsp;by:&nbsp;BRAIN&nbsp;-&nbsp;Brazilian&nbsp;Artificial&nbsp;Inteligence&nbsp;Nucleus<br>
--------------------------------------------------------------<br>
Developers:&nbsp;Natanael&nbsp;Vitorino,&nbsp;Lucas&nbsp;Oliveira&nbsp;and&nbsp;Pedro&nbsp;Santos<br>
---<br>
e-mail:&nbsp;natanael.vitorino@facens.br,&nbsp;lucas.camargo@facens.br&nbsp;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;and&nbsp;pedro.santos@facens.br<br>
---&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br>
BRAIN,&nbsp;Sorocaba,&nbsp;Brazil,&nbsp;2023<br>
--------------------------------------------------------------<br>
Description:&nbsp;A&nbsp;system&nbsp;for&nbsp;processing&nbsp;text&nbsp;on&nbsp;invoices,&nbsp;with&nbsp;<br>
the&nbsp;aim&nbsp;of&nbsp;identifying&nbsp;relevant&nbsp;fields&nbsp;on&nbsp;an&nbsp;invoice&nbsp;and&nbsp;<br>
optimizing&nbsp;rebate&nbsp;or&nbsp;validation&nbsp;systems.&nbsp;Making&nbsp;life&nbsp;easier&nbsp;<br>
for&nbsp;logistics&nbsp;operators,&nbsp;merchants&nbsp;and&nbsp;managers,&nbsp;the&nbsp;<br>
application&nbsp;has&nbsp;an&nbsp;interface&nbsp;that&nbsp;captures&nbsp;webcam&nbsp;images,&nbsp;<br>
processes&nbsp;the&nbsp;image&nbsp;using&nbsp;OCR&nbsp;and&nbsp;makes&nbsp;it&nbsp;possible&nbsp;to&nbsp;view&nbsp;<br>
the&nbsp;results&nbsp;obtained.<br>
...<br>
OCR&nbsp;PROCESSING</tt></p>
<p>
<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="section">
<tr bgcolor="#aa55cc">
<td colspan=3 valign=bottom>&nbsp;<br>
<font color="#ffffff" face="helvetica, arial"><big><strong>Modules</strong></big></font></td></tr>
    
<tr><td bgcolor="#aa55cc"><tt>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</tt></td><td>&nbsp;</td>
<td width="100%"><table width="100%" summary="list"><tr><td width="25%" valign=top><a href="cv2.html">cv2</a><br>
</td><td width="25%" valign=top><a href="numpy.html">numpy</a><br>
</td><td width="25%" valign=top></td><td width="25%" valign=top></td></tr></table></td></tr></table><p>
<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="section">
<tr bgcolor="#ee77aa">
<td colspan=3 valign=bottom>&nbsp;<br>
<font color="#ffffff" face="helvetica, arial"><big><strong>Classes</strong></big></font></td></tr>
    
<tr><td bgcolor="#ee77aa"><tt>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</tt></td><td>&nbsp;</td>
<td width="100%"><dl>
<dt><font face="helvetica, arial"><a href="builtins.html#object">builtins.object</a>
</font></dt><dd>
<dl>
<dt><font face="helvetica, arial"><a href="utils.html#Filter">Filter</a>
</font></dt><dt><font face="helvetica, arial"><a href="utils.html#Results">Results</a>
</font></dt></dl>
</dd>
</dl>
 <p>
<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="section">
<tr bgcolor="#ffc8d8">
<td colspan=3 valign=bottom>&nbsp;<br>
<font color="#000000" face="helvetica, arial"><a name="Filter">class <strong>Filter</strong></a>(<a href="builtins.html#object">builtins.object</a>)</font></td></tr>
    
<tr bgcolor="#ffc8d8"><td rowspan=2><tt>&nbsp;&nbsp;&nbsp;</tt></td>
<td colspan=2><tt><a href="#Filter">Filter</a>(filter_:&nbsp;List[str])<br>
&nbsp;<br>
<a href="#Filter">Filter</a>&nbsp;for&nbsp;selecting&nbsp;words&nbsp;that&nbsp;the&nbsp;user&nbsp;wants&nbsp;to&nbsp;find&nbsp;from&nbsp;the&nbsp;words&nbsp;found&nbsp;by&nbsp;OCR&nbsp;processing.<br>
&nbsp;<br>
...<br>
Attributes<br>
----------<br>
_filter_words&nbsp;:&nbsp;list<br>
&nbsp;&nbsp;&nbsp;&nbsp;Words&nbsp;to&nbsp;filter.<br>
&nbsp;<br>
Methods<br>
-------<br>
&nbsp;&nbsp;&nbsp;&nbsp;<a href="#Filter-set_filter">set_filter</a>(new_filter)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Save&nbsp;words&nbsp;to&nbsp;filtering,&nbsp;setter&nbsp;to&nbsp;_filter_words&nbsp;(variable)<br>
&nbsp;&nbsp;&nbsp;&nbsp;<a href="#Filter-get_filter">get_filter</a>()<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Returns&nbsp;the&nbsp;filter&nbsp;words<br>&nbsp;</tt></td></tr>
<tr><td>&nbsp;</td>
<td width="100%">Methods defined here:<br>
<dl><dt><a name="Filter-__init__"><strong>__init__</strong></a>(self, filter_: List[str])</dt><dd><tt>Constructor&nbsp;for&nbsp;filter&nbsp;words&nbsp;class.<br>
&nbsp;<br>
...<br>
Args:<br>
&nbsp;&nbsp;&nbsp;&nbsp;Without&nbsp;args.<br>
&nbsp;<br>
Returns:<br>
&nbsp;&nbsp;&nbsp;&nbsp;Without&nbsp;returns..</tt></dd></dl>

<dl><dt><a name="Filter-get_filter"><strong>get_filter</strong></a>(self)</dt><dd><tt>Getter&nbsp;for&nbsp;filter&nbsp;words.<br>
&nbsp;<br>
...<br>
Args:<br>
&nbsp;&nbsp;&nbsp;&nbsp;Without&nbsp;args.<br>
&nbsp;<br>
Returns:<br>
&nbsp;&nbsp;&nbsp;&nbsp;The&nbsp;filter&nbsp;words.</tt></dd></dl>

<dl><dt><a name="Filter-set_filter"><strong>set_filter</strong></a>(self, new_filter)</dt><dd><tt>Setter&nbsp;for&nbsp;filter&nbsp;words.<br>
&nbsp;<br>
...<br>
Args:<br>
&nbsp;&nbsp;&nbsp;&nbsp;Without&nbsp;args.<br>
&nbsp;<br>
Returns:<br>
&nbsp;&nbsp;&nbsp;&nbsp;Without&nbsp;returns.</tt></dd></dl>

<hr>
Data descriptors defined here:<br>
<dl><dt><strong>__dict__</strong></dt>
<dd><tt>dictionary&nbsp;for&nbsp;instance&nbsp;variables&nbsp;(if&nbsp;defined)</tt></dd>
</dl>
<dl><dt><strong>__weakref__</strong></dt>
<dd><tt>list&nbsp;of&nbsp;weak&nbsp;references&nbsp;to&nbsp;the&nbsp;object&nbsp;(if&nbsp;defined)</tt></dd>
</dl>
</td></tr></table> <p>
<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="section">
<tr bgcolor="#ffc8d8">
<td colspan=3 valign=bottom>&nbsp;<br>
<font color="#000000" face="helvetica, arial"><a name="Results">class <strong>Results</strong></a>(<a href="builtins.html#object">builtins.object</a>)</font></td></tr>
    
<tr bgcolor="#ffc8d8"><td rowspan=2><tt>&nbsp;&nbsp;&nbsp;</tt></td>
<td colspan=2><tt><a href="#Filter">Filter</a>&nbsp;for&nbsp;selecting&nbsp;words&nbsp;that&nbsp;the&nbsp;user&nbsp;wants&nbsp;to&nbsp;find&nbsp;from&nbsp;the&nbsp;words&nbsp;found&nbsp;by&nbsp;OCR&nbsp;processing.<br>
&nbsp;<br>
...<br>
Attributes<br>
----------<br>
_filter_words&nbsp;:&nbsp;list<br>
&nbsp;&nbsp;&nbsp;&nbsp;Words&nbsp;to&nbsp;filter.<br>
&nbsp;<br>
Methods<br>
-------<br>
&nbsp;&nbsp;&nbsp;&nbsp;set_filter(new_filter)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Save&nbsp;words&nbsp;to&nbsp;filtering,&nbsp;setter&nbsp;to&nbsp;_filter_words&nbsp;(variable)<br>
&nbsp;&nbsp;&nbsp;&nbsp;get_filter()<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Returns&nbsp;the&nbsp;filter&nbsp;words<br>&nbsp;</tt></td></tr>
<tr><td>&nbsp;</td>
<td width="100%">Methods defined here:<br>
<dl><dt><a name="Results-__init__"><strong>__init__</strong></a>(self)</dt><dd><tt>Constructor&nbsp;to&nbsp;<a href="#Results">Results</a>&nbsp;class<br>
&nbsp;<br>
...<br>
Args:<br>
&nbsp;&nbsp;&nbsp;&nbsp;None<br>
&nbsp;<br>
Returns:<br>
&nbsp;&nbsp;&nbsp;&nbsp;None</tt></dd></dl>

<dl><dt><a name="Results-get_results"><strong>get_results</strong></a>(self)</dt><dd><tt>Getter&nbsp;for&nbsp;OCR&nbsp;processing&nbsp;results.<br>
&nbsp;<br>
...<br>
Args:<br>
&nbsp;&nbsp;&nbsp;&nbsp;Without&nbsp;args.<br>
&nbsp;<br>
Returns:<br>
&nbsp;&nbsp;&nbsp;&nbsp;The&nbsp;results.</tt></dd></dl>

<dl><dt><a name="Results-set_results"><strong>set_results</strong></a>(self, new_results)</dt><dd><tt>Setter&nbsp;for&nbsp;OCR&nbsp;processing&nbsp;results.<br>
&nbsp;<br>
...<br>
Args:<br>
&nbsp;&nbsp;&nbsp;&nbsp;new_results&nbsp;:&nbsp;<a href="#Results">Results</a>&nbsp;from&nbsp;OCR&nbsp;processing.<br>
&nbsp;<br>
Returns:<br>
&nbsp;&nbsp;&nbsp;&nbsp;without&nbsp;return.</tt></dd></dl>

<hr>
Data descriptors defined here:<br>
<dl><dt><strong>__dict__</strong></dt>
<dd><tt>dictionary&nbsp;for&nbsp;instance&nbsp;variables&nbsp;(if&nbsp;defined)</tt></dd>
</dl>
<dl><dt><strong>__weakref__</strong></dt>
<dd><tt>list&nbsp;of&nbsp;weak&nbsp;references&nbsp;to&nbsp;the&nbsp;object&nbsp;(if&nbsp;defined)</tt></dd>
</dl>
</td></tr></table></td></tr></table><p>
<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="section">
<tr bgcolor="#eeaa77">
<td colspan=3 valign=bottom>&nbsp;<br>
<font color="#ffffff" face="helvetica, arial"><big><strong>Functions</strong></big></font></td></tr>
    
<tr><td bgcolor="#eeaa77"><tt>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</tt></td><td>&nbsp;</td>
<td width="100%"><dl><dt><a name="-filter_process"><strong>filter_process</strong></a>(result, phrases)</dt><dd><tt><a href="#Filter">Filter</a>&nbsp;processing.<br>
&nbsp;<br>
...<br>
Args:<br>
&nbsp;&nbsp;&nbsp;&nbsp;img:&nbsp;image&nbsp;to&nbsp;process.<br>
&nbsp;&nbsp;&nbsp;&nbsp;phrases:&nbsp;words&nbsp;filter.<br>
&nbsp;<br>
Returns:<br>
&nbsp;&nbsp;&nbsp;&nbsp;The&nbsp;word&nbsp;of&nbsp;interest&nbsp;based&nbsp;on&nbsp;the&nbsp;filter&nbsp;reference.</tt></dd></dl>
 <dl><dt><a name="-list_of_strings"><strong>list_of_strings</strong></a>(arg)</dt><dd><tt>Get&nbsp;list&nbsp;of&nbsp;strings&nbsp;from&nbsp;user's&nbsp;filter&nbsp;input.<br>
&nbsp;<br>
...<br>
Args:<br>
&nbsp;&nbsp;&nbsp;&nbsp;arg:&nbsp;Words&nbsp;taken&nbsp;from&nbsp;user&nbsp;input.<br>
&nbsp;<br>
Returns:<br>
&nbsp;&nbsp;&nbsp;&nbsp;The&nbsp;words&nbsp;entered&nbsp;by&nbsp;the&nbsp;user.</tt></dd></dl>
 <dl><dt><a name="-ocr_process"><strong>ocr_process</strong></a>(img)</dt><dd><tt>OCR&nbsp;processing.<br>
&nbsp;<br>
...<br>
Args:<br>
&nbsp;&nbsp;&nbsp;&nbsp;Frame&nbsp;with&nbsp;rgb&nbsp;color&nbsp;pattern&nbsp;and&nbsp;processed&nbsp;from&nbsp;byte&nbsp;array&nbsp;to&nbsp;ndarray.</tt></dd></dl>
</td></tr></table><p>
<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="section">
<tr bgcolor="#55aa55">
<td colspan=3 valign=bottom>&nbsp;<br>
<font color="#ffffff" face="helvetica, arial"><big><strong>Data</strong></big></font></td></tr>
    
<tr><td bgcolor="#55aa55"><tt>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</tt></td><td>&nbsp;</td>
<td width="100%"><strong>List</strong> = typing.List</td></tr></table>
</body></html>
...<br>
Args:<br>
&nbsp;&nbsp;&nbsp;&nbsp;data:&nbsp;API&nbsp;buffer&nbsp;image.<br>
&nbsp;<br>
Returns:<br>
&nbsp;&nbsp;&nbsp;&nbsp;Frame&nbsp;with&nbsp;rgb&nbsp;color&nbsp;pattern&nbsp;and&nbsp;processed&nbsp;from&nbsp;byte&nbsp;array&nbsp;to&nbsp;ndarray.</tt></dd></dl>
</td></tr></table><p>
<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="section">
<tr bgcolor="#55aa55">
<td colspan=3 valign=bottom>&nbsp;<br>
<font color="#ffffff" face="helvetica, arial"><big><strong>Data</strong></big></font></td></tr>
    
<tr><td bgcolor="#55aa55"><tt>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</tt></td><td>&nbsp;</td>
<td width="100%"><strong>List</strong> = typing.List</td></tr></table>
</body></html>