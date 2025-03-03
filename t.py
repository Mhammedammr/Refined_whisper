from models import llm

text = """


<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head><title>

</title><script type="text/javascript" src="/ClinicalSheetWebSite/ruxitagentjs_ICA27NVfgjqrux_10259230221142207.js" data-dtconfig="rid=RID_-1812804122|rpid=-2073033207|reportUrl=/ClinicalSheetWebSite/rb_bf74291bjy|app=ea7c4b59f27d43eb|featureHash=ICA27NVfgjqrux|vcv=2|rdnt=1|uxrgce=1|bp=3|cuc=nwy952og|mel=100000|dpvc=1|ssv=4|lastModification=1678585915823|dtVersion=10259230221142207|tp=500,50,0,1|uxdcw=1500|agentUri=/ClinicalSheetWebSite/ruxitagentjs_ICA27NVfgjqrux_10259230221142207.js"></script><link href="../Theme/css/SheetsLayout.css" rel="stylesheet" />
    <script src="../Scripts/jquery-1.10.2.min.js" type="text/javascript"></script>
    
    <style type="text/css">
        .auto-style1 {
            font-size: x-large;
            text-decoration: underline;
        }
        .auto-style2 {
            width: 93px;
        }
        .auto-style3 {
            width: 233px;
        }
        .auto-style4 {
            width: 572px;
        }
        .auto-style5 {
            width: 640px;
        }
        .auto-style6 {
            width: 132px;
        }
        .auto-style7 {
            width: 1922px;
        }
        .auto-style8 {
            width: 196px;
        }
        .auto-style9 {
            width: 100%;
        }
        .auto-style10 {
            width: 223px;
        }
        .auto-style11 {
            width: 239px;
        }
        .auto-style13 {
            width: 365px;
        }
        .auto-style14 {
            width: 303px;
        }
        .auto-style15 {
            width: 351px;
        }
        .auto-style16 {
            width: 195px;
        }
        .auto-style17 {
            width: 165px;
        }
        .auto-style18 {
            width: 187px;
        }
    </style>

    <style type="text/css">
         @media screen {#SheetMainDiv {height: 312px; }}
         @media print 
        { 
      * {font-family: 'Source Sans Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif !important;font-size:12px;}
       .RadLabel {font-size: 14px;float: right;margin-top: 3px !important; }
       *{line-height: 28px !important;font-size:17px !important;}
             .clinicalSheet input[type="checkbox"] {
    -webkit-appearance: none;
    border: 1px solid #7f7f7f;
    padding: 6px;
    display: inline-block;
    position: relative;
    
   
    border-width: 1px;
    border-style: solid;
    width: 0.8em;
    height: 0.8em;
    font-size: 1em;
    line-height: 1em;
    text-align: center; }
	  .clinicalSheet input[type="checkbox"]:checked:after {
        content: "\2713";
        font-size: 16px;
        position: absolute;
        top: -8px;
        left: 2px;
        color: #000; }

        } 
    </style>
    
<link href="/ClinicalSheetWebSite/WebResource.axd?d=bZQu9IErOfGRZdP9C3BB5Yfbg7qzMQBQqYhjgAqy84rMiEDYllZB0y1DJZ2eAbdRqt0wI2zKE0NlGN9b0Aa80zMnXjmbawBMvcduHxrrgs80MHKOuNgjn3sv1EY5Zpwy0&amp;t=636999118760000000" type="text/css" rel="stylesheet" class="Telerik_stylesheet" /><link href="/ClinicalSheetWebSite/WebResource.axd?d=EkHr37SACCjvnXcRDMYA5cdIK9kxC9l5n1IACJS5ygMTII44IepOKqvwcyBkntMRHw3Dc2hD9octg73RgttUaIdjFJstG2Y7GLDfsZ9usmpKCa-HNXd2-85CREuSWncynW-wcepZOWvpSU6aqqc7gA2&amp;t=636999118760000000" type="text/css" rel="stylesheet" class="Telerik_stylesheet" /><link href="/ClinicalSheetWebSite/WebResource.axd?d=AvBWCtbpLXYjyyNienFv2MNMa2GwH2lB1chrYeq3ShimPltGU1757REFevL-qat_oL8SCTmRGWiKQiirztqLFmanDsYvaaUkBEB6m5gPl3s1Q6QGHIQ4QPvruMr20l49I8Z4j6Jgp4TbnnpJa2oErg2&amp;t=636999118760000000" type="text/css" rel="stylesheet" class="Telerik_stylesheet" /><link href="/ClinicalSheetWebSite/WebResource.axd?d=QioIuMiTvakjAw8Q44fnHrQAqt0Gt7fd6MlF7yXw_q3hg7a5QcYaTpTuk5VHAH31NTM8WkBWE-rAsD1zqhXW2bFt-VoOgwZL-EeWEqAxSesn8mUBiW3Xn8a2BQhgNqIOqFio6Y_VGBxgkNNxGPeghG3_oQm6_Iyak45EPdqhMlw1&amp;t=636999118760000000" type="text/css" rel="stylesheet" class="Telerik_stylesheet" /></head>
<body class="clinicalSheet">
    <form method="post" action="./Confidential - Adolescent Health Raaps?visitID=0" id="formSheet">
<input type="hidden" name="RadScriptManager1_TSM" id="RadScriptManager1_TSM" value="" />
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="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" />


<script src="/ClinicalSheetWebSite/Telerik.Web.UI.WebResource.axd?_TSM_HiddenField_=RadScriptManager1_TSM&amp;compress=1&amp;_TSM_CombinedScripts_=%3b%3bSystem.Web.Extensions%2c+Version%3d4.0.0.0%2c+Culture%3dneutral%2c+PublicKeyToken%3d31bf3856ad364e35%3aen-US%3a2caafa8b-6f58-4a66-a3cd-4d77ee6a1707%3aea597d4b%3bTelerik.Web.UI%3aen-US%3af8fbf82e-0050-4b46-80b2-4fd09c29f9d6%3a16e4e7cd%3af7645509%3a22a6274a%3a33715776%3a8674cba1%3a7c926187%3a88144a7a%3ab7778d6c%3ac08e9f8a%3a59462f1%3aa51ee93e" type="text/javascript"></script>
<input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="0B5A613D" />
<input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="hEso+wRquRwzTQgkOaX3FZknFr/z0G+asITf1ecRROEsayGnBl06Qp14FoP33EJXlJOaRBJlqetZUItZfa9I3Xmkjfx911FdPcMVt0MtO2s/++JGRZy8eHmrt6lkK3DE0ek+vVd/KG4hSpt3ipTcvsAW/cRZ1pw34t+vwIDVXZnvBIZhj68jX6SfRhaJboxvrXy+zwuItpI1sZOg/+QiS9szx1qehl0dKtLbG4UiABOUlbqePKJjEuQ0pYi5bStsLPedvKdhGZYujXR2WI3DyH8Bf01y6whSfsvH12S+7lrOoKQobodS9eUOCvlZcn3psSDK/p7svmXh1JwDElA13+T8w4MRSGgq1Nww2BiD4W7F8v/f+42zF4kDP95arTjmlfh+mqhLFwdq2bmUa+swNlxoBTS6NfH/fDh5suZY1Ae09Vd0ZMWmUlW+IIzEjvycs4A9Ui4tzfSfaUY7hI3LlI/1A3LHB0yfNt0r1mqN8dnKUPxywwLSs7adAVHyE/fA6s9ZAdfGTOTxuz8GvcqjRe/sk2j+kM4wqbYDczumdIYeogyHnXcCxFPtjedpb0lWv8ez6NbAziTdEUl9FdpIgfur8naL1I1a7Wm3TFkE7TaX0dpTYHTofvSUho1Cb8Ug6wiw/D9W0ZZQyP/ao9Qaa6cd5U9rSeYovAA8LGnzmOa7i6RXkrhdpt+pYdzXzLQG/JsbnbYvhaq/gJXtS50vqa0k+RtvF1vjVOnUw9wFu3AhIuCikkalD2EDaOn9zulQc+NmIhvaCE9eCB/Mmp3P9FUbuYffg7t34Tu6xVfusRN2MQSeJw/m0cCCBMm1MMWhG+T6h09Tvd2fvOhA91VgM8Bi2EBi7sH6vzmvJNW/+6WQxbbsybP7KxHdtu2dFHVTtUNmV7mbd8hUaXb5/yuIKfWt/9DkH/aD8pBJNyJb46vEqu3K1jr2QPf0dsSp/Fg6l84ka75J2Dsre7ixOWWNu7J978XD7W5H+2s6Z67S72q7/ruFHyc3wCfi7XRBXNFGdVpsIoJnHYhJsNIyfJ6Uo7Oxf9sdVNeZ/yqZAFVS4eQUmAr3OfZfDxglXtr48FKYtpjA8UhNIfO6Uv/itlzilDjisV8HUQZFr8pH8sr5XZZ6bt+jQDK5eIk22EQWJMrNSzJPEONj88Rn6dwf1sAu2+vaAcWqovJDdtnNafc0fwUJqDL9CZSPtGQDmotOLxLRT6zxnSV7SyA7OKDLZcedy3d4Ti3ObVJJfZSv2qBYwd0VWHvcvGTaVzPsdqQKKiEjAknp3w0HtPRlm65qTbLcb+DJ3TWGTPRB32HVxUGE+XEoE9pkwY6N3qosZbUts344zU7MW96mOvwRIlvHj5GPhpkG6KNwfCd131FBK7j5naepP1XUiDuekAnjoPwX/NXGGjJfrr1Wf+geCbna9lVHQ/tKyTC9TpqyEbCtFpWnAGs8gSL24xGljepiLzM0Rlhafs+eRCp+ucwJPg4Dk/NIZZocuURs0s+vWqSPykU3HzWBrNxTG4Vk4ypReAS2JMWWDg/Gvh+VUPCNsr84xBIaMZNTndkAeHQ/l4ifOhslC8hlyrJj9x58EE8MLh/19buoI8zWb6Td+30UpZ/zgZZVPFjUOcnD2foB9m8vQVbDQQN3p8jiwFnYZN0tDC8RIf3O4wQG0wq/dtTAWJzb+wzchQj30SjDWiSB5WSn01w95ek=" />
            
    <div id="SheetMainDiv">
        
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; <strong><span class="auto-style1" style="text-align: center">Confidential - Adolescent Health Raaps</span></strong><br />
    <br />
    <br />
    <table style="width:100%;" border="1" title="Information">
        <tr>
            <td class="auto-style2" style="font-weight: bold">Name:</td>
            <td>
                <input name="ctl00$SheetContentPlaceHolder$TextBox1" type="text" id="SheetContentPlaceHolder_TextBox1" />
            </td>
            <td class="auto-style3" style="font-weight: bold">Insurance:</td>
            <td class="auto-style4">
                <input name="ctl00$SheetContentPlaceHolder$TextBox4" type="text" id="SheetContentPlaceHolder_TextBox4" />
            </td>
        </tr>
        <tr>
            <td class="auto-style2" style="font-weight: bold">Brithdate:</td>
            <td>
                <input name="ctl00$SheetContentPlaceHolder$TextBox2" type="text" id="SheetContentPlaceHolder_TextBox2" />
            </td>
            <td class="auto-style3" style="font-weight: bold">Ethnicity/Race:</td>
            <td class="auto-style4">
                <input name="ctl00$SheetContentPlaceHolder$TextBox5" type="text" id="SheetContentPlaceHolder_TextBox5" />
            </td>
        </tr>
        <tr>
            <td class="auto-style2" style="font-weight: bold">Sex:</td>
            <td>
                <input name="ctl00$SheetContentPlaceHolder$TextBox3" type="text" id="SheetContentPlaceHolder_TextBox3" />
            </td>
            <td class="auto-style3" style="font-weight: bold">Registration#:</td>
            <td class="auto-style4">
                <input name="ctl00$SheetContentPlaceHolder$TextBox6" type="text" id="SheetContentPlaceHolder_TextBox6" />
            </td>
        </tr>
    </table>
    <table border="1" style="width:100%;">
        <tr>
            <td class="auto-style5" style="font-weight: bold">Health Risk Profile: Confidential</td>
            <td style="font-weight: bold">Your answers will only be seen by the center staff</td>
        </tr>
    </table>
    <table border="1" class="auto-style9">
        <tr>
            <td class="auto-style6" style="font-weight: bold; text-align: center;">Question NO.</td>
            <td class="auto-style7" style="font-weight: bold; text-align: center;">Questions</td>
            <td class="auto-style8" style="font-weight: bold; text-align: center;">Your Answer</td>
        </tr>
        <tr>
            <td class="auto-style6" style="font-size: medium; text-align: center; font-weight: bold;">1</td>
            <td class="auto-style7" style="font-size: medium; text-align: center; font-weight: bold;">In the past 12 months, have you tried to lose weight by obsessively exercising, taking diet pills or laxatives, making yourself vomit (throw up) after eating, or starving yourself?</td>
            <td class="auto-style8">
                <span id="SheetContentPlaceHolder_RadioButtonList2" style="display:inline-block;"><b><font size="4"><input id="SheetContentPlaceHolder_RadioButtonList2_0" type="radio" name="ctl00$SheetContentPlaceHolder$RadioButtonList2" value="Yes" /><label for="SheetContentPlaceHolder_RadioButtonList2_0">Yes</label><input id="SheetContentPlaceHolder_RadioButtonList2_1" type="radio" name="ctl00$SheetContentPlaceHolder$RadioButtonList2" value="No" /><label for="SheetContentPlaceHolder_RadioButtonList2_1">No</label></font></b></span>
            </td>
        </tr>
        <tr>
            <td class="auto-style6" style="font-size: medium; text-align: center; font-weight: bold;">2</td>
            <td class="auto-style7" style="font-size: medium; text-align: center; font-weight: bold;">Do you eat some fruits and vegetables every day?</td>
            <td class="auto-style8">
                <span id="SheetContentPlaceHolder_RadioButtonList1" style="display:inline-block;"><b><font size="4"><input id="SheetContentPlaceHolder_RadioButtonList1_0" type="radio" name="ctl00$SheetContentPlaceHolder$RadioButtonList1" value="Yes" /><label for="SheetContentPlaceHolder_RadioButtonList1_0">Yes</label><input id="SheetContentPlaceHolder_RadioButtonList1_1" type="radio" name="ctl00$SheetContentPlaceHolder$RadioButtonList1" value="No" /><label for="SheetContentPlaceHolder_RadioButtonList1_1">No</label></font></b></span>
            </td>
        </tr>
        <tr>
            <td class="auto-style6" style="font-size: medium; text-align: center; font-weight: bold;">3</td>
            <td class="auto-style7" style="font-size: medium; text-align: center; font-weight: bold;">Are you active after school or on weekends (walking, running, dancing, swimming, biking, playing sports) for at least 1 hour, on at least 3 or more days each week?</td>
            <td class="auto-style8">
                <span id="SheetContentPlaceHolder_RadioButtonList3" style="display:inline-block;"><b><font size="4"><input id="SheetContentPlaceHolder_RadioButtonList3_0" type="radio" name="ctl00$SheetContentPlaceHolder$RadioButtonList3" value="Yes" /><label for="SheetContentPlaceHolder_RadioButtonList3_0">Yes</label><input id="SheetContentPlaceHolder_RadioButtonList3_1" type="radio" name="ctl00$SheetContentPlaceHolder$RadioButtonList3" value="No" /><label for="SheetContentPlaceHolder_RadioButtonList3_1">No</label></font></b></span>
            </td>
        </tr>
        <tr>
            <td class="auto-style6" style="font-size: medium; text-align: center; font-weight: bold;">4</td>
            <td class="auto-style7" style="font-size: medium; text-align: center; font-weight: bold;">Do you always wear a lap/seat belt when you are driving or riding in a car, truck, or van?</td>
            <td class="auto-style8">
                <span id="SheetContentPlaceHolder_RadioButtonList4" style="display:inline-block;"><b><font size="4"><input id="SheetContentPlaceHolder_RadioButtonList4_0" type="radio" name="ctl00$SheetContentPlaceHolder$RadioButtonList4" value="Yes" /><label for="SheetContentPlaceHolder_RadioButtonList4_0">Yes</label><input id="SheetContentPlaceHolder_RadioButtonList4_1" type="radio" name="ctl00$SheetContentPlaceHolder$RadioButtonList4" value="No" /><label for="SheetContentPlaceHolder_RadioButtonList4_1">No</label></font></b></span>
            </td>
        </tr>
        <tr>
            <td class="auto-style6" style="font-size: medium; text-align: center; font-weight: bold;">5</td>
            <td class="auto-style7" style="font-size: medium; text-align: center; font-weight: bold;">Do you always wear a helmet when you are biking, rollerblading, skateboarding, motorcycling, snowmobiling, skiing or snowboarding?</td>
            <td class="auto-style8">
                <span id="SheetContentPlaceHolder_RadioButtonList5" style="display:inline-block;"><b><font size="4"><input id="SheetContentPlaceHolder_RadioButtonList5_0" type="radio" name="ctl00$SheetContentPlaceHolder$RadioButtonList5" value="Yes" /><label for="SheetContentPlaceHolder_RadioButtonList5_0">Yes</label><input id="SheetContentPlaceHolder_RadioButtonList5_1" type="radio" name="ctl00$SheetContentPlaceHolder$RadioButtonList5" value="No" /><label for="SheetContentPlaceHolder_RadioButtonList5_1">No</label></font></b></span>
            </td>
        </tr>
        <tr>
            <td class="auto-style6" style="font-size: medium; text-align: center; font-weight: bold;">6</td>
            <td class="auto-style7" style="font-size: medium; text-align: center; font-weight: bold;">During the past month, have you been threatened, teased, or hurt by someone (on the internet, by text, or in person) or has anyone made you feel sad, unsafe, or afraid?</td>
            <td class="auto-style8">
                <span id="SheetContentPlaceHolder_RadioButtonList6" style="display:inline-block;"><b><font size="4"><input id="SheetContentPlaceHolder_RadioButtonList6_0" type="radio" name="ctl00$SheetContentPlaceHolder$RadioButtonList6" value="Yes" /><label for="SheetContentPlaceHolder_RadioButtonList6_0">Yes</label><input id="SheetContentPlaceHolder_RadioButtonList6_1" type="radio" name="ctl00$SheetContentPlaceHolder$RadioButtonList6" value="No" /><label for="SheetContentPlaceHolder_RadioButtonList6_1">No</label></font></b></span>
            </td>
        </tr>
        <tr>
            <td class="auto-style6" style="font-size: medium; text-align: center; font-weight: bold;">7</td>
            <td class="auto-style7" style="font-size: medium; text-align: center; font-weight: bold;">Has anyone ever abused you physically (hit, slapped, kicked), emotionally (threatened or made you feel afraid) or forced you to have sex or be involved in sexual activities when you didn&#39;t want to?</td>
            <td class="auto-style8">
                <span id="SheetContentPlaceHolder_RadioButtonList7" style="display:inline-block;"><b><font size="4"><input id="SheetContentPlaceHolder_RadioButtonList7_0" type="radio" name="ctl00$SheetContentPlaceHolder$RadioButtonList7" value="Yes" /><label for="SheetContentPlaceHolder_RadioButtonList7_0">Yes</label><input id="SheetContentPlaceHolder_RadioButtonList7_1" type="radio" name="ctl00$SheetContentPlaceHolder$RadioButtonList7" value="No" /><label for="SheetContentPlaceHolder_RadioButtonList7_1">No</label></font></b></span>
            </td>
        </tr>
        <tr>
            <td class="auto-style6" style="font-size: medium; text-align: center; font-weight: bold;">8</td>
            <td class="auto-style7" style="font-size: medium; text-align: center; font-weight: bold;">Have you ever carried a weapon (gun, knife, club, other) to protect yourself?</td>
            <td class="auto-style8">
                <span id="SheetContentPlaceHolder_RadioButtonList8" style="display:inline-block;"><b><font size="4"><input id="SheetContentPlaceHolder_RadioButtonList8_0" type="radio" name="ctl00$SheetContentPlaceHolder$RadioButtonList8" value="Yes" /><label for="SheetContentPlaceHolder_RadioButtonList8_0">Yes</label><input id="SheetContentPlaceHolder_RadioButtonList8_1" type="radio" name="ctl00$SheetContentPlaceHolder$RadioButtonList8" value="No" /><label for="SheetContentPlaceHolder_RadioButtonList8_1">No</label></font></b></span>
            </td>
        </tr>
        <tr>
            <td class="auto-style6" style="font-size: medium; text-align: center; font-weight: bold;">9</td>
            <td class="auto-style7" style="font-size: medium; text-align: center; font-weight: bold;">In the past 3 months, have you smoked cigarettes or any other form of tobacco (cigars, black and mild, hookah, other) or chewed/used smokeless tobacco?</td>
            <td class="auto-style8">
                <span id="SheetContentPlaceHolder_RadioButtonList9" style="display:inline-block;"><b><font size="4"><input id="SheetContentPlaceHolder_RadioButtonList9_0" type="radio" name="ctl00$SheetContentPlaceHolder$RadioButtonList9" value="Yes" /><label for="SheetContentPlaceHolder_RadioButtonList9_0">Yes</label><input id="SheetContentPlaceHolder_RadioButtonList9_1" type="radio" name="ctl00$SheetContentPlaceHolder$RadioButtonList9" value="No" /><label for="SheetContentPlaceHolder_RadioButtonList9_1">No</label></font></b></span>
            </td>
        </tr>
        <tr>
            <td class="auto-style6" style="font-size: medium; text-align: center; font-weight: bold;">10</td>
            <td class="auto-style7" style="font-size: medium; text-align: center; font-weight: bold;">In the past 12 months, have you driven a car drunk, high, or while texting or ridden in a car with a driver who was?</td>
            <td class="auto-style8">
                <span id="SheetContentPlaceHolder_RadioButtonList10" style="display:inline-block;"><b><font size="4"><input id="SheetContentPlaceHolder_RadioButtonList10_0" type="radio" name="ctl00$SheetContentPlaceHolder$RadioButtonList10" value="Yes" /><label for="SheetContentPlaceHolder_RadioButtonList10_0">Yes</label><input id="SheetContentPlaceHolder_RadioButtonList10_1" type="radio" name="ctl00$SheetContentPlaceHolder$RadioButtonList10" value="No" /><label for="SheetContentPlaceHolder_RadioButtonList10_1">No</label></font></b></span>
            </td>
        </tr>
        <tr>
            <td class="auto-style6" style="font-size: medium; text-align: center; font-weight: bold;">11</td>
            <td class="auto-style7" style="font-size: medium; text-align: center; font-weight: bold;">In the past 3 months, have you drunk more than a few sips of alcohol (beer, wine coolers, liquor, other)?</td>
            <td class="auto-style8">
                <span id="SheetContentPlaceHolder_RadioButtonList11" style="display:inline-block;"><b><font size="4"><input id="SheetContentPlaceHolder_RadioButtonList11_0" type="radio" name="ctl00$SheetContentPlaceHolder$RadioButtonList11" value="Yes" /><label for="SheetContentPlaceHolder_RadioButtonList11_0">Yes</label><input id="SheetContentPlaceHolder_RadioButtonList11_1" type="radio" name="ctl00$SheetContentPlaceHolder$RadioButtonList11" value="No" /><label for="SheetContentPlaceHolder_RadioButtonList11_1">No</label></font></b></span>
            </td>
        </tr>
        <tr>
            <td class="auto-style6" style="font-size: medium; text-align: center; font-weight: bold;">12</td>
            <td class="auto-style7" style="font-size: medium; text-align: center; font-weight: bold;">In the past 3 months, have you smoked marijuana, used other street drugs, steroids, or sniffed inhalants (&quot;huffed&quot; household products)?</td>
            <td class="auto-style8">
                <span id="SheetContentPlaceHolder_RadioButtonList12" style="display:inline-block;"><b><font size="4"><input id="SheetContentPlaceHolder_RadioButtonList12_0" type="radio" name="ctl00$SheetContentPlaceHolder$RadioButtonList12" value="Yes" /><label for="SheetContentPlaceHolder_RadioButtonList12_0">Yes</label><input id="SheetContentPlaceHolder_RadioButtonList12_1" type="radio" name="ctl00$SheetContentPlaceHolder$RadioButtonList12" value="No" /><label for="SheetContentPlaceHolder_RadioButtonList12_1">No</label></font></b></span>
            </td>
        </tr>
        <tr>
            <td class="auto-style6" style="font-size: medium; text-align: center; font-weight: bold;">13</td>
            <td class="auto-style7" style="font-size: medium; text-align: center; font-weight: bold;">In the past 3 months, have you used someone else&#39;s prescription (from a doctor or other health provider) or any nonprescription (from a store) drugs to sleep, stay awake, concentrate, calm down, or get high?</td>
            <td class="auto-style8">
                <span id="SheetContentPlaceHolder_RadioButtonList13" style="display:inline-block;"><b><font size="4"><input id="SheetContentPlaceHolder_RadioButtonList13_0" type="radio" name="ctl00$SheetContentPlaceHolder$RadioButtonList13" value="Yes" /><label for="SheetContentPlaceHolder_RadioButtonList13_0">Yes</label><input id="SheetContentPlaceHolder_RadioButtonList13_1" type="radio" name="ctl00$SheetContentPlaceHolder$RadioButtonList13" value="No" /><label for="SheetContentPlaceHolder_RadioButtonList13_1">No</label></font></b></span>
            </td>
        </tr>
        <tr>
            <td class="auto-style6" style="font-size: medium; text-align: center; font-weight: bold;">14</td>
            <td class="auto-style7" style="font-size: medium; text-align: center; font-weight: bold;">Have you ever had any type of sex (vaginal, anal or oral sex)?</td>
            <td class="auto-style8">
                <span id="SheetContentPlaceHolder_RadioButtonList14" style="display:inline-block;"><b><font size="4"><input id="SheetContentPlaceHolder_RadioButtonList14_0" type="radio" name="ctl00$SheetContentPlaceHolder$RadioButtonList14" value="Yes" /><label for="SheetContentPlaceHolder_RadioButtonList14_0">Yes</label><input id="SheetContentPlaceHolder_RadioButtonList14_1" type="radio" name="ctl00$SheetContentPlaceHolder$RadioButtonList14" value="No" /><label for="SheetContentPlaceHolder_RadioButtonList14_1">No</label></font></b></span>
            </td>
        </tr>
        <tr>
            <td class="auto-style6" style="font-size: medium; text-align: center; font-weight: bold;">15</td>
            <td class="auto-style7" style="font-size: medium; text-align: center; font-weight: bold;">Have you ever been attracted to the same sex (girl to girl/guy to guy) or do you feel that you are gay, lesbian, or bisexual?</td>
            <td class="auto-style8">
                <span id="SheetContentPlaceHolder_RadioButtonList15" style="display:inline-block;"><b><font size="4"><input id="SheetContentPlaceHolder_RadioButtonList15_0" type="radio" name="ctl00$SheetContentPlaceHolder$RadioButtonList15" value="Yes" /><label for="SheetContentPlaceHolder_RadioButtonList15_0">Yes</label><input id="SheetContentPlaceHolder_RadioButtonList15_1" type="radio" name="ctl00$SheetContentPlaceHolder$RadioButtonList15" value="No" /><label for="SheetContentPlaceHolder_RadioButtonList15_1">No</label></font></b></span>
            </td>
        </tr>
        <tr>
            <td class="auto-style6" style="font-size: medium; text-align: center; font-weight: bold;">16</td>
            <td class="auto-style7" style="font-size: medium; text-align: center; font-weight: bold;">If you have had sex, do you always use a method to prevent sexually transmitted infections and pregnancy (condoms, female barriers, other)?</td>
            <td class="auto-style8">
                <span id="SheetContentPlaceHolder_RadioButtonList16" style="display:inline-block;"><b><font size="4"><input id="SheetContentPlaceHolder_RadioButtonList16_0" type="radio" name="ctl00$SheetContentPlaceHolder$RadioButtonList16" value="Yes" /><label for="SheetContentPlaceHolder_RadioButtonList16_0">Yes</label><input id="SheetContentPlaceHolder_RadioButtonList16_1" type="radio" name="ctl00$SheetContentPlaceHolder$RadioButtonList16" value="No" /><label for="SheetContentPlaceHolder_RadioButtonList16_1">No</label></font></b></span>
            </td>
        </tr>
        <tr>
            <td class="auto-style6" style="font-size: medium; text-align: center; font-weight: bold;">17</td>
            <td class="auto-style7" style="font-size: medium; text-align: center; font-weight: bold;">During the past month, did you often feel sad or down as though you had nothing to look forÂ¬ward to?</td>
            <td class="auto-style8">
                <span id="SheetContentPlaceHolder_RadioButtonList17" style="display:inline-block;"><b><font size="4"><input id="SheetContentPlaceHolder_RadioButtonList17_0" type="radio" name="ctl00$SheetContentPlaceHolder$RadioButtonList17" value="Yes" /><label for="SheetContentPlaceHolder_RadioButtonList17_0">Yes</label><input id="SheetContentPlaceHolder_RadioButtonList17_1" type="radio" name="ctl00$SheetContentPlaceHolder$RadioButtonList17" value="No" /><label for="SheetContentPlaceHolder_RadioButtonList17_1">No</label></font></b></span>
            </td>
        </tr>
        <tr>
            <td class="auto-style6" style="font-size: medium; text-align: center; font-weight: bold;">18</td>
            <td class="auto-style7" style="font-size: medium; text-align: center; font-weight: bold;">Do you have any serious problems or worries at home or at school?</td>
            <td class="auto-style8">
                <span id="SheetContentPlaceHolder_RadioButtonList18" style="display:inline-block;"><b><font size="4"><input id="SheetContentPlaceHolder_RadioButtonList18_0" type="radio" name="ctl00$SheetContentPlaceHolder$RadioButtonList18" value="Yes" /><label for="SheetContentPlaceHolder_RadioButtonList18_0">Yes</label><input id="SheetContentPlaceHolder_RadioButtonList18_1" type="radio" name="ctl00$SheetContentPlaceHolder$RadioButtonList18" value="No" /><label for="SheetContentPlaceHolder_RadioButtonList18_1">No</label></font></b></span>
            </td>
        </tr>
        <tr>
            <td class="auto-style6" style="font-size: medium; text-align: center; font-weight: bold;">19</td>
            <td class="auto-style7" style="font-size: medium; text-align: center; font-weight: bold;">In the past 12 months, have you seriously thought about killing yourself, tried to kill yourself, or have you purposely cut, burned or otherwise hurt yourself?</td>
            <td class="auto-style8">
                <span id="SheetContentPlaceHolder_RadioButtonList19" style="display:inline-block;"><b><font size="4"><input id="SheetContentPlaceHolder_RadioButtonList19_0" type="radio" name="ctl00$SheetContentPlaceHolder$RadioButtonList19" value="Yes" /><label for="SheetContentPlaceHolder_RadioButtonList19_0">Yes</label><input id="SheetContentPlaceHolder_RadioButtonList19_1" type="radio" name="ctl00$SheetContentPlaceHolder$RadioButtonList19" value="No" /><label for="SheetContentPlaceHolder_RadioButtonList19_1">No</label></font></b></span>
            </td>
        </tr>
        <tr>
            <td class="auto-style6" style="font-size: medium; text-align: center; font-weight: bold;">20</td>
            <td class="auto-style7" style="font-size: medium; text-align: center; font-weight: bold;">Do you have at least one adult in your life that you can talk to about any problems or worries?</td>
            <td class="auto-style8">
                <span id="SheetContentPlaceHolder_RadioButtonList20" style="display:inline-block;"><b><font size="4"><input id="SheetContentPlaceHolder_RadioButtonList20_0" type="radio" name="ctl00$SheetContentPlaceHolder$RadioButtonList20" value="Yes" /><label for="SheetContentPlaceHolder_RadioButtonList20_0">Yes</label><input id="SheetContentPlaceHolder_RadioButtonList20_1" type="radio" name="ctl00$SheetContentPlaceHolder$RadioButtonList20" value="No" /><label for="SheetContentPlaceHolder_RadioButtonList20_1">No</label></font></b></span>
            </td>
        </tr>
        <tr>
            <td class="auto-style6" style="font-size: medium; text-align: center; font-weight: bold;">21</td>
            <td class="auto-style7" style="font-size: medium; text-align: center; font-weight: bold;">When you are angry, do you do things that get you in trouble?</td>
            <td class="auto-style8">
                <span id="SheetContentPlaceHolder_RadioButtonList21" style="display:inline-block;"><b><font size="4"><input id="SheetContentPlaceHolder_RadioButtonList21_0" type="radio" name="ctl00$SheetContentPlaceHolder$RadioButtonList21" value="Yes" /><label for="SheetContentPlaceHolder_RadioButtonList21_0">Yes</label><input id="SheetContentPlaceHolder_RadioButtonList21_1" type="radio" name="ctl00$SheetContentPlaceHolder$RadioButtonList21" value="No" /><label for="SheetContentPlaceHolder_RadioButtonList21_1">No</label></font></b></span>
            </td>
        </tr>
    </table>
    <br />
    <table class="auto-style9">
        <tr>
            <td colspan="3" style="font-size: medium; font-weight: bold">For Office Use Only</td>
            <td class="auto-style14" style="font-size: medium; font-weight: bold">&nbsp;</td>
            <td class="auto-style17" style="font-size: medium; font-weight: bold">&nbsp;</td>
            <td class="auto-style13" style="font-size: medium; font-weight: bold">&nbsp;</td>
            <td class="auto-style16" style="font-size: medium; font-weight: bold">&nbsp;</td>
            <td class="auto-style15" style="font-size: medium; font-weight: bold">&nbsp;</td>
        </tr>
        <tr>
            <td class="auto-style10" style="font-size: medium; font-weight: bold">At Risk Counseled</td>
            <td class="auto-style11">
                <input name="ctl00$SheetContentPlaceHolder$TextBox7" type="text" id="SheetContentPlaceHolder_TextBox7" />
            </td>
            <td class="auto-style18" style="font-size: medium; font-weight: bold">At Risk Needs f/u:</td>
            <td class="auto-style14">
                <input name="ctl00$SheetContentPlaceHolder$TextBox11" type="text" id="SheetContentPlaceHolder_TextBox11" />
            </td>
            <td class="auto-style17" style="font-size: medium; font-weight: bold">No Current Risk:</td>
            <td class="auto-style13">
                <input name="ctl00$SheetContentPlaceHolder$TextBox9" type="text" id="SheetContentPlaceHolder_TextBox9" />
            </td>
            <td class="auto-style16" style="font-size: medium; font-weight: bold">Referred to:</td>
            <td class="auto-style15">
                <input name="ctl00$SheetContentPlaceHolder$TextBox10" type="text" id="SheetContentPlaceHolder_TextBox10" />
            </td>
            <td></td>
        </tr>
        <tr>
            <td class="auto-style10" style="font-size: medium; font-weight: bold">Provider Signature: </td>
            <td class="auto-style11">
                <input name="ctl00$SheetContentPlaceHolder$TextBox12" type="text" id="SheetContentPlaceHolder_TextBox12" />
            </td>
            <td class="auto-style18" style="font-size: medium; font-weight: bold">Date</td>
            <td class="auto-style14">
                <div id="ctl00_SheetContentPlaceHolder_RadDatePicker1_wrapper" class="RadPicker RadPicker_Default" style="display:inline-block;width:93px;">
	<!-- 2017.2.621.45 --><input style="visibility:hidden;display:block;float:right;margin:0 0 -1px -1px;width:1px;height:1px;overflow:hidden;border:0;padding:0;" id="ctl00_SheetContentPlaceHolder_RadDatePicker1" name="ctl00$SheetContentPlaceHolder$RadDatePicker1" type="text" class="rdfd_ radPreventDecorate" value="" title="Visually hidden input created for functionality purposes." /><table cellspacing="0" class="rcTable rcSingle" summary="Table holding date picker control for selection of dates." style="width:100%;">
		<caption style="display:none;">
			RadDatePicker
		</caption><thead style="display:none;">
			<tr>
				<th scope="col">RadDatePicker</th>
			</tr>
		</thead><tbody>
			<tr>
				<td class="rcInputCell" style="width:100%;"><span id="ctl00_SheetContentPlaceHolder_RadDatePicker1_dateInput_wrapper" class="riSingle RadInput RadInput_Default" style="display:block;width:100%;"><input id="ctl00_SheetContentPlaceHolder_RadDatePicker1_dateInput" name="ctl00$SheetContentPlaceHolder$RadDatePicker1$dateInput" class="riTextBox riEnabled" type="text" /><input id="ctl00_SheetContentPlaceHolder_RadDatePicker1_dateInput_ClientState" name="ctl00_SheetContentPlaceHolder_RadDatePicker1_dateInput_ClientState" type="hidden" /></span></td><td><a title="Open the calendar popup." href="#" id="ctl00_SheetContentPlaceHolder_RadDatePicker1_popupButton" class="rcCalPopup">Open the calendar popup.</a><div id="ctl00_SheetContentPlaceHolder_RadDatePicker1_calendar_wrapper" style="display:none;">
					<table id="ctl00_SheetContentPlaceHolder_RadDatePicker1_calendar" cellspacing="0" class="RadCalendar RadCalendar_Default">
						<caption>
							<span style='display:none;'>Calendar</span>
						</caption><thead>
							<tr>
								<td class="rcTitlebar"><table cellspacing="0">
									<caption>
										<span style='display:none;'>Title and navigation</span>
									</caption><thead>
										<tr style="display:none;">
											<th scope="col">Title and navigation</th>
										</tr>
									</thead><tbody>
	<tr>
		<td><a id="ctl00_SheetContentPlaceHolder_RadDatePicker1_calendar_FNP" class="t-button rcFastPrev" title="&lt;&lt;" href="#">&lt;&lt;</a></td><td><a id="ctl00_SheetContentPlaceHolder_RadDatePicker1_calendar_NP" class="t-button rcPrev" title="&lt;" href="#">&lt;</a></td><td id="ctl00_SheetContentPlaceHolder_RadDatePicker1_calendar_Title" class="rcTitle">March, 2023</td><td><a id="ctl00_SheetContentPlaceHolder_RadDatePicker1_calendar_NN" class="t-button rcNext" title=">" href="#">&gt;</a></td><td><a id="ctl00_SheetContentPlaceHolder_RadDatePicker1_calendar_FNN" class="t-button rcFastNext" title=">>" href="#">&lt;&lt;</a></td>
	</tr>
</tbody>
								</table></td>
							</tr>
						</thead><tbody>
	<tr>
		<td class="rcMain"><table id="ctl00_SheetContentPlaceHolder_RadDatePicker1_calendar_Top" class="rcMainTable" cellspacing="0">
	<caption>
		<span style='display:none;'>March, 2023</span>
	</caption><thead>
		<tr class="rcWeek">
			<th class="rcViewSel" scope="col">&nbsp;</th><th id="ctl00_SheetContentPlaceHolder_RadDatePicker1_calendar_Top_cs_1" title="Sunday" scope="col">S</th><th id="ctl00_SheetContentPlaceHolder_RadDatePicker1_calendar_Top_cs_2" title="Monday" scope="col">M</th><th id="ctl00_SheetContentPlaceHolder_RadDatePicker1_calendar_Top_cs_3" title="Tuesday" scope="col">T</th><th id="ctl00_SheetContentPlaceHolder_RadDatePicker1_calendar_Top_cs_4" title="Wednesday" scope="col">W</th><th id="ctl00_SheetContentPlaceHolder_RadDatePicker1_calendar_Top_cs_5" title="Thursday" scope="col">T</th><th id="ctl00_SheetContentPlaceHolder_RadDatePicker1_calendar_Top_cs_6" title="Friday" scope="col">F</th><th id="ctl00_SheetContentPlaceHolder_RadDatePicker1_calendar_Top_cs_7" title="Saturday" scope="col">S</th>
		</tr>
	</thead><tbody>
		<tr class="rcRow">
			<th id="ctl00_SheetContentPlaceHolder_RadDatePicker1_calendar_Top_rs_1" scope="row">9</th><td class="rcOtherMonth" title="Sunday, February 26, 2023"><a href="#">26</a></td><td class="rcOtherMonth" title="Monday, February 27, 2023"><a href="#">27</a></td><td class="rcOtherMonth" title="Tuesday, February 28, 2023"><a href="#">28</a></td><td title="Wednesday, March 01, 2023"><a href="#">1</a></td><td title="Thursday, March 02, 2023"><a href="#">2</a></td><td title="Friday, March 03, 2023"><a href="#">3</a></td><td class="rcWeekend" title="Saturday, March 04, 2023"><a href="#">4</a></td>
		</tr><tr class="rcRow">
			<th id="ctl00_SheetContentPlaceHolder_RadDatePicker1_calendar_Top_rs_2" scope="row">10</th><td class="rcWeekend" title="Sunday, March 05, 2023"><a href="#">5</a></td><td title="Monday, March 06, 2023"><a href="#">6</a></td><td title="Tuesday, March 07, 2023"><a href="#">7</a></td><td title="Wednesday, March 08, 2023"><a href="#">8</a></td><td title="Thursday, March 09, 2023"><a href="#">9</a></td><td title="Friday, March 10, 2023"><a href="#">10</a></td><td class="rcWeekend" title="Saturday, March 11, 2023"><a href="#">11</a></td>
		</tr><tr class="rcRow">
			<th id="ctl00_SheetContentPlaceHolder_RadDatePicker1_calendar_Top_rs_3" scope="row">11</th><td class="rcWeekend" title="Sunday, March 12, 2023"><a href="#">12</a></td><td title="Monday, March 13, 2023"><a href="#">13</a></td><td title="Tuesday, March 14, 2023"><a href="#">14</a></td><td title="Wednesday, March 15, 2023"><a href="#">15</a></td><td title="Thursday, March 16, 2023"><a href="#">16</a></td><td title="Friday, March 17, 2023"><a href="#">17</a></td><td class="rcWeekend" title="Saturday, March 18, 2023"><a href="#">18</a></td>
		</tr><tr class="rcRow">
			<th id="ctl00_SheetContentPlaceHolder_RadDatePicker1_calendar_Top_rs_4" scope="row">12</th><td class="rcWeekend" title="Sunday, March 19, 2023"><a href="#">19</a></td><td title="Monday, March 20, 2023"><a href="#">20</a></td><td title="Tuesday, March 21, 2023"><a href="#">21</a></td><td title="Wednesday, March 22, 2023"><a href="#">22</a></td><td title="Thursday, March 23, 2023"><a href="#">23</a></td><td title="Friday, March 24, 2023"><a href="#">24</a></td><td class="rcWeekend" title="Saturday, March 25, 2023"><a href="#">25</a></td>
		</tr><tr class="rcRow">
			<th id="ctl00_SheetContentPlaceHolder_RadDatePicker1_calendar_Top_rs_5" scope="row">13</th><td class="rcWeekend" title="Sunday, March 26, 2023"><a href="#">26</a></td><td title="Monday, March 27, 2023"><a href="#">27</a></td><td title="Tuesday, March 28, 2023"><a href="#">28</a></td><td title="Wednesday, March 29, 2023"><a href="#">29</a></td><td title="Thursday, March 30, 2023"><a href="#">30</a></td><td title="Friday, March 31, 2023"><a href="#">31</a></td><td class="rcOtherMonth" title="Saturday, April 01, 2023"><a href="#">1</a></td>
		</tr><tr class="rcRow">
			<th id="ctl00_SheetContentPlaceHolder_RadDatePicker1_calendar_Top_rs_6" scope="row">14</th><td class="rcOtherMonth" title="Sunday, April 02, 2023"><a href="#">2</a></td><td class="rcOtherMonth" title="Monday, April 03, 2023"><a href="#">3</a></td><td class="rcOtherMonth" title="Tuesday, April 04, 2023"><a href="#">4</a></td><td class="rcOtherMonth" title="Wednesday, April 05, 2023"><a href="#">5</a></td><td class="rcOtherMonth" title="Thursday, April 06, 2023"><a href="#">6</a></td><td class="rcOtherMonth" title="Friday, April 07, 2023"><a href="#">7</a></td><td class="rcOtherMonth" title="Saturday, April 08, 2023"><a href="#">8</a></td>
		</tr>
	</tbody>
</table></td>
	</tr>
</tbody>
					</table><input type="hidden" name="ctl00_SheetContentPlaceHolder_RadDatePicker1_calendar_SD" id="ctl00_SheetContentPlaceHolder_RadDatePicker1_calendar_SD" value="[]" /><input type="hidden" name="ctl00_SheetContentPlaceHolder_RadDatePicker1_calendar_AD" id="ctl00_SheetContentPlaceHolder_RadDatePicker1_calendar_AD" value="[[1980,1,1],[2099,12,30],[2023,3,12]]" />
				</div></td>
			</tr>
		</tbody>
	</table><input id="ctl00_SheetContentPlaceHolder_RadDatePicker1_ClientState" name="ctl00_SheetContentPlaceHolder_RadDatePicker1_ClientState" type="hidden" />
</div>
            </td>
        </tr>
    </table>
    <br />
    <br />
    <br />
    <br />
    <br />
    <br />

        
    </div>
    

<script type="text/javascript">
//<![CDATA[
Sys.Application.add_init(function() {
    $create(Telerik.Web.UI.RadDateInput, {"_displayText":"","_focused":false,"_initialValueAsText":"","_postBackEventReferenceScript":"__doPostBack(\u0027ctl00$SheetContentPlaceHolder$RadDatePicker1\u0027,\u0027\u0027)","_skin":"Default","_validationText":"","clientStateFieldID":"ctl00_SheetContentPlaceHolder_RadDatePicker1_dateInput_ClientState","dateFormat":"M/d/yyyy","dateFormatInfo":{"DayNames":["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],"MonthNames":["January","February","March","April","May","June","July","August","September","October","November","December",""],"AbbreviatedDayNames":["Sun","Mon","Tue","Wed","Thu","Fri","Sat"],"AbbreviatedMonthNames":["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec",""],"AMDesignator":"AM","PMDesignator":"PM","DateSeparator":"/","TimeSeparator":":","FirstDayOfWeek":0,"DateSlots":{"Day":1,"Year":2,"Month":0},"ShortYearCenturyEnd":2029,"TimeInputOnly":false,"MonthYearOnly":false},"displayDateFormat":"M/d/yyyy","enabled":true,"incrementSettings":{InterceptArrowKeys:true,InterceptMouseWheel:true,Step:1},"styles":{HoveredStyle: ["width:100%;", "riTextBox riHover"],InvalidStyle: ["width:100%;", "riTextBox riError"],DisabledStyle: ["width:100%;", "riTextBox riDisabled"],FocusedStyle: ["width:100%;", "riTextBox riFocused"],EmptyMessageStyle: ["width:100%;", "riTextBox riEmpty"],ReadOnlyStyle: ["width:100%;", "riTextBox riRead"],EnabledStyle: ["width:100%;", "riTextBox riEnabled"]}}, null, null, $get("ctl00_SheetContentPlaceHolder_RadDatePicker1_dateInput"));
});
Sys.Application.add_init(function() {
    $create(Telerik.Web.UI.RadCalendar, {"_DayRenderChangedDays":{},"_FormatInfoArray":[["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],["Sun","Mon","Tue","Wed","Thu","Fri","Sat"],["January","February","March","April","May","June","July","August","September","October","November","December",""],["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec",""],"dddd, MMMM dd, yyyy h:mm:ss tt","dddd, MMMM dd, yyyy","h:mm:ss tt","MMMM dd","ddd, dd MMM yyyy HH\u0027:\u0027mm\u0027:\u0027ss \u0027GMT\u0027","M/d/yyyy","h:mm tt","yyyy\u0027-\u0027MM\u0027-\u0027dd\u0027T\u0027HH\u0027:\u0027mm\u0027:\u0027ss","yyyy\u0027-\u0027MM\u0027-\u0027dd HH\u0027:\u0027mm\u0027:\u0027ss\u0027Z\u0027","MMMM, yyyy","AM","PM","/",":",0],"_ViewRepeatableDays":{},"_ViewsHash":{"ctl00_SheetContentPlaceHolder_RadDatePicker1_calendar_Top" : [[2023,3,1], 1]},"_calendarWeekRule":0,"_culture":"en-US","_enableKeyboardNavigation":false,"_enableViewSelector":false,"_firstDayOfWeek":7,"_postBackCall":"__doPostBack(\u0027ctl00$SheetContentPlaceHolder$RadDatePicker1$calendar\u0027,\u0027@@\u0027)","_rangeSelectionMode":0,"clientStateFieldID":"ctl00_SheetContentPlaceHolder_RadDatePicker1_calendar_ClientState","enableMultiSelect":false,"enabled":true,"monthYearNavigationSettings":["Today","OK","Cancel","Date is out of range.","False","True","300","1","300","1","False"],"skin":"Default","specialDaysArray":[],"stylesHash":{"DayStyle": ["", ""],"CalendarTableStyle": ["", "rcMainTable"],"OtherMonthDayStyle": ["", "rcOtherMonth"],"TitleStyle": ["", ""],"SelectedDayStyle": ["", "rcSelected"],"SelectorStyle": ["", ""],"DisabledDayStyle": ["", "rcDisabled"],"OutOfRangeDayStyle": ["", "rcOutOfRange"],"WeekendDayStyle": ["", "rcWeekend"],"DayOverStyle": ["", "rcHover"],"FastNavigationStyle": ["", "RadCalendarMonthView RadCalendarMonthView_Default"],"ViewSelectorStyle": ["", "rcViewSel"]},"titleFormat":"MMMM, yyyy","useColumnHeadersAsSelectors":false,"useRowHeadersAsSelectors":false}, null, null, $get("ctl00_SheetContentPlaceHolder_RadDatePicker1_calendar"));
});
Sys.Application.add_init(function() {
    $create(Telerik.Web.UI.RadDatePicker, {"_PopupButtonSettings":{ ResolvedImageUrl : "", ResolvedHoverImageUrl : ""},"_animationSettings":{ShowAnimationDuration:300,ShowAnimationType:1,HideAnimationDuration:300,HideAnimationType:1},"_popupControlID":"ctl00_SheetContentPlaceHolder_RadDatePicker1_popupButton","clientStateFieldID":"ctl00_SheetContentPlaceHolder_RadDatePicker1_ClientState","focusedDate":"2023-03-12-00-00-00"}, null, {"calendar":"ctl00_SheetContentPlaceHolder_RadDatePicker1_calendar","dateInput":"ctl00_SheetContentPlaceHolder_RadDatePicker1_dateInput"}, $get("ctl00_SheetContentPlaceHolder_RadDatePicker1"));
});
//]]>
</script>
</form>
            <script>
        $(document).ready(function () {
            $(".RadEditor").removeClass("Default").addClass("Bootstrap");
            $(".reToolbarWrapper").removeClass("Default").addClass("Bootstrap");
            $(".reToolbar").removeClass("Default").addClass("Bootstrap");
            // remove unwanted controls from rad editor // 
            $(".RadEditor .FindAndReplace,.RadEditor .Print,.RadEditor .AjaxSpellCheck,.RadEditor .SelectAll,.RadEditor .Copy").parents("li").hide();
            $(".RadEditor .Cut,.RadEditor .Paste,.RadEditor .PasteStrip,.RadEditor .Undo,.RadEditor .Redo").parents("li").hide();
            $(".RadEditor .DocumentManager,.RadEditor .FlashManager,.RadEditor .MediaManager,.RadEditor .TemplateManager,.RadEditor .Superscript").parents("li").hide();
            $(".RadEditor .Subscript,.RadEditor .InsertParagraph,.RadEditor .InsertGroupbox,.RadEditor .InsertHorizontalRule,.RadEditor .InsertDate").parents("li").hide();
            $(".RadEditor .InsertTime,.RadEditor .FormatCodeBlock,.RadEditor .AbsolutePosition,.RadEditor .Zoom,.RadEditor .ModuleManager").parents("li").hide();
            $(".RadEditor .ToggleTableBorder,.RadEditor .XhtmlValidator,.RadEditor .ApplyClass,.RadEditor .InsertSymbol,.RadEditor .InsertFormElement").parents("li").hide();
            $(".RadEditor .InsertSnippet,.RadEditor .ImageMapDialog,.RadEditor .InsertCustomLink,.RadEditor .ConvertToLower,.RadEditor .ConvertToUpper").parents("li").hide();
            $(".RadEditor .ToggleScreenMode,.RadEditor .AboutDialog,.RadEditor .Outdent,.RadEditor .FormatStripper").parents("li").hide();
            $(".RadEditor .reEditorModesCell").parent("tr").hide();
            // end of remove unwanted controls from rad editor //
            // remove unwanted controls from rad image editor // 
            $(".RadImageEditor .riePrint,.RadImageEditor .rieReset").parent("li").hide();
            // end of remove unwanted controls from rad image editor //
        })
    </script>

</body>
</html>

"""
from . import models
file_path = "waves/wave2.m4a"
# raw_text = LLM.speech_reco(audio_file_path=file_path)

json_data = models.llm(task="text", raw_text=text)
print(json_data)
refined_text = models.llm(task="voice", raw_text="""The patient is a 32-year-old married male with a 10-year smoking history
                        who does not consume alcohol or caffeine. He has a family history of diabetes in his mother and an
                        anxiety disorder in his sister, with no known significant diseases in his father, grandparents,
                        or children. The patient has a medical history of chronic Factor VIII deficiency (hemophilia A), asthma,
                        and a mild milk allergy. His current medications include codeine, morphine, and Factor VIII replacement
                        therapy. He presented to the hospital with a chief complaint of severe knee pain, rated 8/10 on the pain
                        scale, which has persisted for several weeks, along with difficulty sleeping and trouble performing physical
                        activities such as walking and climbing stairs. His vital signs include a blood pressure of 128/76 mmHg, heart rate
                        of 88 bpm, respiratory rate of 18 breaths/min, temperature of 98.6°F (37°C), and oxygen saturation of 96% on room air.
                        He stands 5’10” (178 cm) tall, weighs 185 lbs (84 kg), and has a BMI of 26.6, placing him in the overweight category.
                        A functional screen revealed significant difficulty with ambulation due to knee pain, requiring a cane for short
                        distances and assistance for longer walks. He reports poor sleep quality, averaging 4-5 hours per night, and struggles 
                       with instrumental activities of daily living such as grocery shopping and household chores due to limited mobility. 
                       The patient has a history of leaving against medical advice (AMA) but denies any sexual dysfunction. His asthma is
                        currently stable, with no recent exacerbations. The assessment includes chronic Factor VIII deficiency with suspected
                        hemarthrosis in the knee, contributing to severe pain and functional limitations, overweight status with potential 
                       impact on joint health, chronic pain management requiring reassessment of long-term opioid use, and stable asthma. 
                       The plan involves further evaluation of the knee with imaging, optimization of pain management, monitoring and adjustment
                        of Factor VIII therapy, smoking cessation counseling, nutritional counseling for weight management, sleep hygiene education,
                        and close follow-up to ensure adherence to treatment and prevent further complications.""", html_text=json_data)

print(refined_text)