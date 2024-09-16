from bs4 import BeautifulSoup
import json

# Sample HTML string (Replace this with actual HTML content)
html_content = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" translate="no">
<head>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-PD11DFYVJC"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-PD11DFYVJC');
</script>

  <meta name="fragment" content="!">
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <meta http-equiv="Content-Language" content="EN"/>
  <meta name="description" content="Hadith of the Prophet Muhammad (saws) in English and Arabic"/>
  <meta name="keywords" content="hadith, hadeeth, sunnah, bukhari, muslim, sahih, sunan, tirmidhi, nawawi, holy, arabic, iman, islam, Allah, book, english"/>
  <meta name="Charset" content="UTF-8"/> 
  <meta name="Distribution" content="Global"/>
  <meta name="Rating" content="General"/>
 
  <meta property="og:image" content="https://sunnah.com/images/hadith_icon2_huge.png" />
  <meta property="og:description" content="Narrated 'Umar bin Al-Khattab:


     I heard Allah's Messenger (ﷺ) saying, &quot;The reward of deeds depends upon the 
     intentions and every person will get the reward according to what he 
     has intended. So whoever emigrated for worldly benefits or for a woman
     to marry, his emigration wa" />
  <meta name="csrf-param" content="_csrf_frontend">
<meta name="csrf-token" content="rMdZKLs2qXmobj_iGi_375317yuWo3bGsOXujGr8jzTFhDpO60LDDcYZT7siTa6l2cSsSeSaOq6FtbTOIovGeA==">

  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="/css/all.css?ver=1708578075" media="screen" rel="stylesheet" type="text/css" />
  
  <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
  <link rel="icon" type="image/png" sizes="128x128" href="/favicon-128x128.png">
  <link rel="image_src" href="/images/hadith_icon2.png" />
  <link rel="apple-touch-icon" href="/images/apple-touch-icon.png" />

  <link rel="stylesheet" href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/themes/base/jquery-ui.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script> 
  <script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js"></script>
  <script src="/js/jquery.cookie.js"></script>
  <!--<script type="text/javascript" src="http://www.google.com/recaptcha/api/js/recaptcha_ajax.js" async></script>-->

  
	<script>
	    var collection = 'bukhari';
	    var bookID = '1';
		var pageType = 'hadithtext';
		var spshowing = true;
		var avbl_languages = ["urdu","bangla"];
	</script>
  	<script>
		</script>
  <script src="/js/sunnah.js?ver=1724478807"></script>
  <!--<script src="https://apis.google.com/js/platform.js" async defer></script>-->
 
  <title>
	Revelation - Sunnah.com - Sayings and Teachings of Prophet Muhammad (صلى الله عليه و سلم)
  </title>
</head>

<body>
<div id="fb-root"></div>
	
<div id="site">
	<div id="header">
    	<div id="toolbar">
       		<div id="toolbarRight">
				            <a href="https://quran.com">Qur'an</a> |
            <a href="https://sunnah.com"><b>Sunnah</b></a> |
            <a href="https://salah.com">Prayer Times</a> |
            <a href="https://quranicaudio.com">Audio</a> 
	        </div>
    	</div>

		<a href="https://sunnah.com"><div id="banner" class=bannerTop></div></a>
		<!-- <a href="#"><div id=back-to-top></div></a> -->
		
<div id=search>
    <a class="searchtipslink">Search Tips</a>
    <div id="searchbar">
        <form name="searchform" action="/search/" method=get id="searchform">
            <input type="text" class="searchquery" name=q placeholder= "Search …" value="" />
            <input type="submit" class="searchsubmit" value="l" />
        </form>
    </div>

	<div id="searchtips">
		<div class=clear></div>
		<b>Quotes</b> e.g. "pledge allegiance"<br>
		Searches for the whole phrase instead of individual words
		<p>
		<b>Wildcards</b> e.g. test*<br>
		Matches any set of one or more characters. For example test* would result in test, tester, testers, etc.
		<p>
		<b>Fuzzy Search</b> e.g. swore~<br>
		Finds terms that are similar in spelling. For example swore~ would result in swore, snore, score, etc.
		<p>
		<b>Term Boosting</b> e.g. pledge^4 hijrah<br>
		Boosts words with higher relevance. Here, the word <i>pledge</i> will have higher weight than <i>hijrah</i>
		<p>
		<b>Boolean Operators</b> e.g. ("pledge allegiance" OR "shelter) AND prayer<br>
		Create complex phrase and word queries by using Boolean logic.
		<p>
		<a href="/searchtips">More ...</a>
	<div class=clear></div>
	</div>
</div>
		<div class=clear></div>
		<div class=crumbs><a href="/">Home</a> &#187; <a href="/bukhari">Sahih al-Bukhari</a> &#187; Revelation</div><div class=clear></div>	</div>

	<div class=clear></div>
	<div id="topspace"></div>

	<div id="nonheader">
	<div class="sidePanelContainer">
		<div style="height: 1px;"></div>
		<div id="sidePanel">
			
<div id="languagePanel">

Language:

<div style="padding-top: 10px;">
	<input type="radio" name="sidelang" value="english" id="ch_english" onclick="toggleLanguageDisplay('english');" checked="checked"  />
    <label for="ch_english">English</label>
</div>             
<!--
<div>
	<input type="checkbox" name="arabic" id="ch_arabic" onclick="" checked="checked" disabled />
    <label for="ch_arabic">Arabic العربية</label>
</div>            
--> 

<div>
	<input type="radio" name="sidelang" value="urdu" id="ch_urdu" onclick="toggleLanguageDisplay('urdu')"  />
    <label for="ch_urdu">Urdu &nbsp;<span style="font-family: Jameel Noori Nastaleeq; font-size: 16px;">اردو</span></label>
</div>             

<div>
	<input type="radio" name="sidelang" value="bangla" id="ch_bangla" onclick="toggleLanguageDisplay('bangla')"  />
    <label for="ch_bangla">Bangla &nbsp;<span style="font-size: 16px;">বাংলা</span></label>
</div>             


</div>
    	</div>
	</div><!-- sidePanelContainer close -->
	<div class="mainContainer"><div id="main">
	        <div class=clear></div>
    <div class="book_info">
    	<div class="book_page_colindextitle">
    		<div class="book_page_arabic_name arabic">كتاب بدء الوحى </div>
			<div class="book_page_number">1&nbsp;&nbsp;</div>    		<div class="book_page_english_name">
				Revelation			</div>
    		<div class=clear></div>
		</div>
    	<div class=clear></div>
		<!-- <div style="width: 20%; float: left; text-align: center; font-size: 20px; padding-top: 16px;"><b>7</b> hadith</div> -->

	
	<div class=clear></div>
	</div>

    
	    <a name="0"></a>
	<div class="AllHadith">
	<a name=C1.00></a>
<div class=chapter>
<div class=echapno>(1)</div><div class=englishchapter>Chapter: How the Divine Revelation started being revealed to Allah's Messenger</div>
<div class=achapno>(1)</div>
<div class="arabicchapter arabic">باب كَيْفَ كَانَ بَدْءُ الْوَحْىِ إِلَى رَسُولِ اللَّهِ صلى الله عليه وسلم</div><div class=clear></div>
</div>
<div class="arabic achapintro aconly">وَقَوْلُ اللَّهِ جَلَّ ذِكْرُهُ: {إِنَّا أَوْحَيْنَا إِلَيْكَ كَمَا أَوْحَيْنَا إِلَى نُوحٍ وَالنَّبِيِّينَ مِنْ بَعْدِهِ}</div>
<div class=clear></div>
<div class="actualHadithContainer hadith_container_bukhari" id=h100010>
<!-- Begin hadith -->

<a name=1></a>
<div class="hadith_reference_sticky">Sahih al-Bukhari 1</div><div class="hadithTextContainers" id=htc100010><div class="englishcontainer" id=t100010><div class="english_hadith_full"><div class=hadith_narrated>Narrated 'Umar bin Al-Khattab:</div><div class=text_details><p>

     I heard Allah's Messenger (ﷺ) saying, "The reward of deeds depends upon the 
     intentions and every person will get the reward according to what he 
     has intended. So whoever emigrated for worldly benefits or for a woman
     to marry, his emigration was for what he emigrated for."
<p></b></div>
<div class=clear></div></div></div><div class="arabic_hadith_full arabic"><span class="arabic_sanad">حَدَّثَنَا<a href="/narrator/4698" title="عبد الله بن الزبير بن عيسى بن عبيد الله بن أسامة بن عبد الله بن حميد بن زهير بن الحارث بن أسد بن عبد العزى" rel="nofollow"> الْحُمَيْدِيُّ عَبْدُ اللَّهِ بْنُ الزُّبَيْرِ  </a>، قَالَ : حَدَّثَنَا<a href="/narrator/3443" title="سفيان بن عيينة بن ميمون" rel="nofollow"> سُفْيَانُ  </a>، قَالَ : حَدَّثَنَا<a href="/narrator/8272" title="يحيى بن سعيد بن قيس بن عمرو بن سهل بن ثعلبة بن الحارث بن زيد بن ثعلبة بن غنم بن مالك بن النجار" rel="nofollow"> يَحْيَى بْنُ سَعِيدٍ الْأَنْصَارِيُّ  </a>، قَالَ : أَخْبَرَنِي<a href="/narrator/6796" title="محمد بن إبراهيم بن الحارث بن خالد بن صخر بن عامر بن كعب بن سعد بن تيم بن مرة" rel="nofollow"> مُحَمَّدُ بْنُ إِبْرَاهِيمَ التَّيْمِيُّ  </a>، أَنَّهُ سَمِعَ<a href="/narrator/5719" title="علقمة بن وقاص بن محصن بن كلدة بن عبد ياليل" rel="nofollow"> عَلْقَمَةَ بْنَ وَقَّاصٍ اللَّيْثِيَّ  </a>، يَقُولُ : سَمِعْتُ<a href="/narrator/5913" title="عمر بن الخطاب بن نفيل بن عبد العزى بن رياح بن عبد الله بن قرط بن رزاح بن عدي بن كعب" rel="nofollow"> عُمَرَ بْنَ الْخَطَّابِ  </a> رَضِيَ اللَّهُ عَنْهُ عَلَى الْمِنْبَرِ، قَالَ : سَمِعْتُ رَسُولَ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ، يَقُولُ : "</span>
<span class="arabic_text_details">إِنَّمَا الْأَعْمَالُ بِالنِّيَّاتِ، وَإِنَّمَا لِكُلِّ امْرِئٍ مَا نَوَى، فَمَنْ كَانَتْ هِجْرَتُهُ إِلَى دُنْيَا يُصِيبُهَا أَوْ إِلَى امْرَأَةٍ يَنْكِحُهَا، فَهِجْرَتُهُ إِلَى مَا هَاجَرَ إِلَيْهِ "</span></div>
</div>
<!-- End hadith -->

<div class="clear"></div><div class=bottomItems>
<table class=hadith_reference cellspacing=0 cellpadding=0><tr><td><b>Reference</b></td><td>&nbsp;:&nbsp;<a href="/bukhari:1">Sahih al-Bukhari 1</a></td></tr><tr><td>In-book reference</td><td>&nbsp;:&nbsp;Book 1, Hadith 1</td></tr><tr><td><span class="deprecated_reference">USC-MSA web (English) reference</span></td><td>&nbsp;: <span class="deprecated_reference">Vol. 1, Book 1, Hadith 1</span></td></tr> <tr><td>&nbsp;&nbsp;<span class="deprecated_reference"><i>(deprecated numbering scheme)</i></span></td></tr></table><div class="hadith_permalink"><span class=reportlink href="javascript: void(0);" onclick="reportHadith(10, 'h100010')">Report Error</span> | <span class=sharelink onclick="share('/bukhari:1')">Share</span> | <span class=copylink title="Copy hadith to clipboard">Copy</span> <span class=copycbcaret title="Change copy options">▼</span></div></div><div class=clear></div></div><!-- end actual hadith container --><div class=clear></div><a name=C2.00></a>
<div class=chapter>
<div class=echapno>(2)</div><div class=englishchapter>Chapter: </div>
<div class=achapno>(2)</div>
<div class="arabicchapter arabic">باب </div><div class=clear></div>
</div>
<div class=clear></div>
<div class="actualHadithContainer hadith_container_bukhari" id=h100020>
<!-- Begin hadith -->

<a name=2></a>
<div class="hadith_reference_sticky">Sahih al-Bukhari 2</div><div class="hadithTextContainers" id=htc100020><div class="englishcontainer" id=t100020><div class="english_hadith_full"><div class=hadith_narrated><p>

     Narrated 'Aisha:</div><div class=text_details><p>

     (the mother of the faithful believers) Al-Harith bin Hisham asked Allah's Messenger (ﷺ) "O Allah's Messenger (ﷺ)! How is the Divine Inspiration revealed to you?" Allah's Messenger (ﷺ) replied, "Sometimes it is (revealed) like the ringing of a bell, this form of Inspiration is the hardest of all and then this state passes off after I have grasped what is inspired. Sometimes the Angel comes in the form of a man and talks to me and I grasp whatever he says." 'Aisha added: Verily I saw the Prophet (ﷺ) being inspired divinely on a very cold day and noticed the sweat dropping from his forehead (as the Inspiration was over).
<p></b></div>
<div class=clear></div></div></div><div class="arabic_hadith_full arabic"><span class="arabic_sanad arabic">حَدَّثَنَا عَبْدُ اللَّهِ بْنُ يُوسُفَ، قَالَ أَخْبَرَنَا مَالِكٌ، عَنْ هِشَامِ بْنِ عُرْوَةَ، عَنْ أَبِيهِ، عَنْ عَائِشَةَ أُمِّ الْمُؤْمِنِينَ ـ رضى الله عنها ـ أَنَّ الْحَارِثَ بْنَ هِشَامٍ ـ رضى الله عنه ـ سَأَلَ رَسُولَ اللَّهِ صلى الله عليه وسلم فَقَالَ يَا رَسُولَ اللَّهِ كَيْفَ يَأْتِيكَ الْوَحْىُ فَقَالَ رَسُولُ اللَّهِ صلى الله عليه وسلم ‏</span>
<span class="arabic_text_details arabic">"‏ أَحْيَانًا يَأْتِينِي مِثْلَ صَلْصَلَةِ الْجَرَسِ ـ وَهُوَ أَشَدُّهُ عَلَىَّ ـ فَيُفْصَمُ عَنِّي وَقَدْ وَعَيْتُ عَنْهُ مَا قَالَ، وَأَحْيَانًا يَتَمَثَّلُ لِيَ الْمَلَكُ رَجُلاً فَيُكَلِّمُنِي فَأَعِي مَا يَقُولُ ‏"</span><span class="arabic_sanad arabic">‏‏.‏ قَالَتْ عَائِشَةُ رضى الله عنها وَلَقَدْ رَأَيْتُهُ يَنْزِلُ عَلَيْهِ الْوَحْىُ فِي الْيَوْمِ الشَّدِيدِ الْبَرْدِ، فَيَفْصِمُ عَنْهُ وَإِنَّ جَبِينَهُ لَيَتَفَصَّدُ عَرَقًا‏.‏</span></div>
</div>
<!-- End hadith -->

<div class="clear"></div><div class=bottomItems>
<table class=hadith_reference cellspacing=0 cellpadding=0><tr><td><b>Reference</b></td><td>&nbsp;:&nbsp;<a href="/bukhari:2">Sahih al-Bukhari 2</a></td></tr><tr><td>In-book reference</td><td>&nbsp;:&nbsp;Book 1, Hadith 2</td></tr><tr><td><span class="deprecated_reference">USC-MSA web (English) reference</span></td><td>&nbsp;: <span class="deprecated_reference">Vol. 1, Book 1, Hadith 2</span></td></tr> <tr><td>&nbsp;&nbsp;<span class="deprecated_reference"><i>(deprecated numbering scheme)</i></span></td></tr></table><div class="hadith_permalink"><span class=reportlink href="javascript: void(0);" onclick="reportHadith(20, 'h100020')">Report Error</span> | <span class=sharelink onclick="share('/bukhari:2')">Share</span> | <span class=copylink title="Copy hadith to clipboard">Copy</span> <span class=copycbcaret title="Change copy options">▼</span></div></div><div class=clear></div></div><!-- end actual hadith container --><div class=clear></div><a name=C3.00></a>
<div class=chapter>
<div class=echapno>(3)</div><div class=englishchapter>Chapter: </div>
<div class=achapno>(3)</div>
<div class="arabicchapter arabic">باب </div><div class=clear></div>
</div>
<div class=clear></div>
<div class="actualHadithContainer hadith_container_bukhari" id=h100030>
<!-- Begin hadith -->

<a name=3></a>
<div class="hadith_reference_sticky">Sahih al-Bukhari 3</div><div class="hadithTextContainers" id=htc100030><div class="englishcontainer" id=t100030><div class="english_hadith_full"><div class=hadith_narrated>Narrated 'Aisha (the mother of the faithful believers):</div><div class=text_details>The commencement of the Divine Inspiration to Allah's Messenger (ﷺ) was in the form of good dreams which came true like bright daylight, and then the love of seclusion was bestowed upon him. He used to go in seclusion in the cave of Hira where he used to worship (Allah alone) continuously for many days before his desire to see his family. He used to take with him the journey food for the stay and then come back to (his wife) Khadija to take his food likewise again till suddenly the Truth descended upon him while he was in the cave of Hira. The angel came to him and asked him to read. The Prophet (ﷺ) replied, "I do not know how to read." The Prophet (ﷺ) added, "The angel caught me (forcefully) and pressed me so hard that I could not bear it any more. He then released me and again asked me to read and I replied, 'I do not know how to read.' Thereupon he caught me again and pressed me a second time till I could not bear it any more. He then released me and again asked me to read but again I replied, 'I do not know how to read (or what shall I read)?' Thereupon he caught me for the third time and pressed me, and then released me and said, 'Read in the name of your Lord, who has created (all that exists), created man from a clot. Read! And your Lord is the Most Generous." (96.1, 96.2, 96.3) Then Allah's Messenger (ﷺ) returned with the Inspiration and with his heart beating severely. Then he went to Khadija bint Khuwailid and said, "Cover me! Cover me!" They covered him till his fear was over and after that he told her everything that had happened and said, "I fear that something may happen to me." Khadija replied, "Never! By Allah, Allah will never disgrace you. You keep good relations with your kith and kin, help the poor and the destitute, serve your guests generously and assist the deserving calamity-afflicted ones."  Khadija then accompanied him to her cousin Waraqa bin Naufal bin Asad bin 'Abdul 'Uzza, who, during the pre-Islamic Period became a Christian and used to write the writing with Hebrew letters. He would write from the Gospel in Hebrew as much as Allah wished him to write. He was an old man and had lost his eyesight. Khadija said to Waraqa, "Listen to the story of your nephew, O my cousin!" Waraqa asked, "O my nephew! What have you seen?" Allah's Messenger (ﷺ) described whatever he had seen. Waraqa said, "This is the same one who keeps the secrets (angel Gabriel) whom Allah had sent to Moses. I wish I were young and could live up to the time when your people would turn you out." Allah's Messenger (ﷺ) asked, "Will they drive me out?" Waraqa replied in the affirmative and said, "Anyone (man) who came with something similar to what you have brought was treated with hostility; and if I should remain alive till the day when you will be turned out then I would support you strongly." But after a few days Waraqa died and the Divine Inspiration was also paused for a while.</b></div>
<div class=clear></div></div></div><div class="arabic_hadith_full arabic"><span class="arabic_sanad arabic"></span>
<span class="arabic_text_details arabic">حَدَّثَنَا يَحْيَى بْنُ بُكَيْرٍ، قَالَ حَدَّثَنَا اللَّيْثُ، عَنْ عُقَيْلٍ، عَنِ ابْنِ شِهَابٍ، عَنْ عُرْوَةَ بْنِ الزُّبَيْرِ، عَنْ عَائِشَةَ أُمِّ الْمُؤْمِنِينَ، أَنَّهَا قَالَتْ أَوَّلُ مَا بُدِئَ بِهِ رَسُولُ اللَّهِ صلى الله عليه وسلم مِنَ الْوَحْىِ الرُّؤْيَا الصَّالِحَةُ فِي النَّوْمِ، فَكَانَ لاَ يَرَى رُؤْيَا إِلاَّ جَاءَتْ مِثْلَ فَلَقِ الصُّبْحِ، ثُمَّ حُبِّبَ إِلَيْهِ الْخَلاَءُ، وَكَانَ يَخْلُو بِغَارِ حِرَاءٍ فَيَتَحَنَّثُ فِيهِ ـ وَهُوَ التَّعَبُّدُ ـ اللَّيَالِيَ ذَوَاتِ الْعَدَدِ قَبْلَ أَنْ يَنْزِعَ إِلَى أَهْلِهِ، وَيَتَزَوَّدُ لِذَلِكَ، ثُمَّ يَرْجِعُ إِلَى خَدِيجَةَ، فَيَتَزَوَّدُ لِمِثْلِهَا، حَتَّى جَاءَهُ الْحَقُّ وَهُوَ فِي غَارِ حِرَاءٍ، فَجَاءَهُ الْمَلَكُ فَقَالَ اقْرَأْ‏.‏ قَالَ ‏"‏ مَا أَنَا بِقَارِئٍ ‏"‏‏.‏ قَالَ ‏"‏ فَأَخَذَنِي فَغَطَّنِي حَتَّى بَلَغَ مِنِّي الْجَهْدَ، ثُمَّ أَرْسَلَنِي فَقَالَ اقْرَأْ‏.‏ قُلْتُ مَا أَنَا بِقَارِئٍ‏.‏ فَأَخَذَنِي فَغَطَّنِي الثَّانِيَةَ حَتَّى بَلَغَ مِنِّي الْجَهْدَ، ثُمَّ أَرْسَلَنِي فَقَالَ اقْرَأْ‏.‏ فَقُلْتُ مَا أَنَا بِقَارِئٍ‏.‏ فَأَخَذَنِي فَغَطَّنِي الثَّالِثَةَ، ثُمَّ أَرْسَلَنِي فَقَالَ <A id="q2" name="q2" href="javascript:openquran(95,1,3)"><c_q2>‏{‏اقْرَأْ بِاسْمِ رَبِّكَ الَّذِي خَلَقَ * خَلَقَ الإِنْسَانَ مِنْ عَلَقٍ * اقْرَأْ وَرَبُّكَ الأَكْرَمُ‏}‏</c_q2></a> ‏"‏‏.‏ فَرَجَعَ بِهَا رَسُولُ اللَّهِ صلى الله عليه وسلم يَرْجُفُ فُؤَادُهُ، فَدَخَلَ عَلَى خَدِيجَةَ بِنْتِ خُوَيْلِدٍ رضى الله عنها فَقَالَ ‏"‏ زَمِّلُونِي زَمِّلُونِي ‏"‏‏.‏ فَزَمَّلُوهُ حَتَّى ذَهَبَ عَنْهُ الرَّوْعُ، فَقَالَ لِخَدِيجَةَ وَأَخْبَرَهَا الْخَبَرَ ‏"‏ لَقَدْ خَشِيتُ عَلَى نَفْسِي ‏"‏‏.‏ فَقَالَتْ خَدِيجَةُ كَلاَّ وَاللَّهِ مَا يُخْزِيكَ اللَّهُ أَبَدًا، إِنَّكَ لَتَصِلُ الرَّحِمَ، وَتَحْمِلُ الْكَلَّ، وَتَكْسِبُ الْمَعْدُومَ، وَتَقْرِي الضَّيْفَ، وَتُعِينُ عَلَى نَوَائِبِ الْحَقِّ‏.‏ فَانْطَلَقَتْ بِهِ خَدِيجَةُ حَتَّى أَتَتْ بِهِ وَرَقَةَ بْنَ نَوْفَلِ بْنِ أَسَدِ بْنِ عَبْدِ الْعُزَّى ابْنَ عَمِّ خَدِيجَةَ ـ وَكَانَ امْرَأً تَنَصَّرَ فِي الْجَاهِلِيَّةِ، وَكَانَ يَكْتُبُ الْكِتَابَ الْعِبْرَانِيَّ، فَيَكْتُبُ مِنَ الإِنْجِيلِ بِالْعِبْرَانِيَّةِ مَا شَاءَ اللَّهُ أَنْ يَكْتُبَ، وَكَانَ شَيْخًا كَبِيرًا قَدْ عَمِيَ ـ فَقَالَتْ لَهُ خَدِيجَةُ يَا ابْنَ عَمِّ اسْمَعْ مِنَ ابْنِ أَخِيكَ‏.‏ فَقَالَ لَهُ وَرَقَةُ يَا ابْنَ أَخِي مَاذَا تَرَى فَأَخْبَرَهُ رَسُولُ اللَّهِ صلى الله عليه وسلم خَبَرَ مَا رَأَى‏.‏ فَقَالَ لَهُ وَرَقَةُ هَذَا النَّامُوسُ الَّذِي نَزَّلَ اللَّهُ عَلَى مُوسَى صلى الله عليه وسلم يَا لَيْتَنِي فِيهَا جَذَعًا، لَيْتَنِي أَكُونُ حَيًّا إِذْ يُخْرِجُكَ قَوْمُكَ‏.‏ فَقَالَ رَسُولُ اللَّهِ صلى الله عليه وسلم ‏"‏ أَوَمُخْرِجِيَّ هُمْ ‏"‏‏.‏ قَالَ نَعَمْ، لَمْ يَأْتِ رَجُلٌ قَطُّ بِمِثْلِ مَا جِئْتَ بِهِ إِلاَّ عُودِيَ، وَإِنْ يُدْرِكْنِي يَوْمُكَ أَنْصُرْكَ نَصْرًا مُؤَزَّرًا‏.‏ ثُمَّ لَمْ يَنْشَبْ وَرَقَةُ أَنْ تُوُفِّيَ وَفَتَرَ الْوَحْىُ‏.‏</span><span class="arabic_sanad arabic"></span></div>
</div>
<!-- End hadith -->

<div class="clear"></div><div class=bottomItems>
<table class=hadith_reference cellspacing=0 cellpadding=0><tr><td><b>Reference</b></td><td>&nbsp;:&nbsp;<a href="/bukhari:3">Sahih al-Bukhari 3</a></td></tr><tr><td>In-book reference</td><td>&nbsp;:&nbsp;Book 1, Hadith 3</td></tr><tr><td><span class="deprecated_reference">USC-MSA web (English) reference</span></td><td>&nbsp;: <span class="deprecated_reference">Vol. 1, Book 1, Hadith 3</span></td></tr> <tr><td>&nbsp;&nbsp;<span class="deprecated_reference"><i>(deprecated numbering scheme)</i></span></td></tr></table><div class="hadith_permalink"><span class=reportlink href="javascript: void(0);" onclick="reportHadith(31, 'h100030')">Report Error</span> | <span class=sharelink onclick="share('/bukhari:3')">Share</span> | <span class=copylink title="Copy hadith to clipboard">Copy</span> <span class=copycbcaret title="Change copy options">▼</span></div></div><div class=clear></div></div><!-- end actual hadith container --><div class=clear></div><div class="actualHadithContainer hadith_container_bukhari" id=h100040>
<!-- Begin hadith -->

<a name=4></a>
<div class="hadith_reference_sticky">Sahih al-Bukhari 4</div><div class="hadithTextContainers" id=htc100040><div class="englishcontainer" id=t100040><div class="english_hadith_full"><div class=hadith_narrated>Narrated Jabir bin 'Abdullah Al-Ansari (while talking about the period of pause in revelation) reporting the speech of the Prophet:</div><div class=text_details>"While I was walking, all of a sudden I heard a voice from the sky. I looked up and saw the same angel who had visited me at the cave of Hira' sitting on a chair between the sky and the earth. I got afraid of him and came back home and said, 'Wrap me (in blankets).' And then Allah revealed the following Holy Verses (of Quran):  'O you (i.e. Muhammad)! wrapped up in garments!' Arise and warn (the people against Allah's Punishment),... up to 'and desert the idols.' (74.1-5) After this the revelation started coming strongly, frequently and regularly."</b></div>
<div class=clear></div></div></div><div class="arabic_hadith_full arabic"><span class="arabic_sanad arabic"></span>
<span class="arabic_text_details arabic">قَالَ ابْنُ شِهَابٍ وَأَخْبَرَنِي أَبُو سَلَمَةَ بْنُ عَبْدِ الرَّحْمَنِ، أَنَّ جَابِرَ بْنَ عَبْدِ اللَّهِ الأَنْصَارِيَّ، قَالَ ـ وَهُوَ يُحَدِّثُ عَنْ فَتْرَةِ الْوَحْىِ، فَقَالَ ـ فِي حَدِيثِهِ ‏"‏ بَيْنَا أَنَا أَمْشِي، إِذْ سَمِعْتُ صَوْتًا، مِنَ السَّمَاءِ، فَرَفَعْتُ بَصَرِي فَإِذَا الْمَلَكُ الَّذِي جَاءَنِي بِحِرَاءٍ جَالِسٌ عَلَى كُرْسِيٍّ بَيْنَ السَّمَاءِ وَالأَرْضِ، فَرُعِبْتُ مِنْهُ، فَرَجَعْتُ فَقُلْتُ زَمِّلُونِي‏.‏ فَأَنْزَلَ اللَّهُ تَعَالَى <A id="q3" name="q3" href="javascript:openquran(73,1,5)"><c_q3>‏{‏يَا أَيُّهَا الْمُدَّثِّرُ * قُمْ فَأَنْذِرْ‏}‏</c_q3></a> إِلَى قَوْلِهِ <A id="q4" name="q4" href="javascript:openquran(73,5,5)"><c_q4>‏{‏وَالرُّجْزَ فَاهْجُرْ‏}‏</c_q4></a> فَحَمِيَ الْوَحْىُ وَتَتَابَعَ ‏"‏‏.‏ تَابَعَهُ عَبْدُ اللَّهِ بْنُ يُوسُفَ وَأَبُو صَالِحٍ‏.‏ وَتَابَعَهُ هِلاَلُ بْنُ رَدَّادٍ عَنِ الزُّهْرِيِّ‏.‏ وَقَالَ يُونُسُ وَمَعْمَرٌ ‏"‏ بَوَادِرُهُ ‏"‏‏.‏</span><span class="arabic_sanad arabic"></span></div>
</div>
<!-- End hadith -->

<div class="clear"></div><div class=bottomItems>
<table class=hadith_reference cellspacing=0 cellpadding=0><tr><td><b>Reference</b></td><td>&nbsp;:&nbsp;<a href="/bukhari:4">Sahih al-Bukhari 4</a></td></tr><tr><td>In-book reference</td><td>&nbsp;:&nbsp;Book 1, Hadith 4</td></tr><tr><td><span class="deprecated_reference">USC-MSA web (English) reference</span></td><td>&nbsp;: <span class="deprecated_reference">Vol. 1, Book 1, Hadith 3</span></td></tr> <tr><td>&nbsp;&nbsp;<span class="deprecated_reference"><i>(deprecated numbering scheme)</i></span></td></tr></table><div class="hadith_permalink"><span class=reportlink href="javascript: void(0);" onclick="reportHadith(32, 'h100040')">Report Error</span> | <span class=sharelink onclick="share('/bukhari:4')">Share</span> | <span class=copylink title="Copy hadith to clipboard">Copy</span> <span class=copycbcaret title="Change copy options">▼</span></div></div><div class=clear></div></div><!-- end actual hadith container --><div class=clear></div><a name=C4.00></a>
<div class=chapter>
<div class=echapno>(4)</div><div class=englishchapter>Chapter: </div>
<div class=achapno>(4)</div>
<div class="arabicchapter arabic">باب </div><div class=clear></div>
</div>
<div class=clear></div>
<div class="actualHadithContainer hadith_container_bukhari" id=h100050>
<!-- Begin hadith -->

<a name=5></a>
<div class="hadith_reference_sticky">Sahih al-Bukhari 5</div><div class="hadithTextContainers" id=htc100050><div class="englishcontainer" id=t100050><div class="english_hadith_full"><div class=hadith_narrated><p>

     Narrated Said bin Jubair:</div><div class=text_details><p>

     Ibn 'Abbas in the explanation of the statement of Allah "Move not your tongue concerning (the Quran) to make haste therewith." (75.16) said "Allah's Messenger (ﷺ) used to bear the revelation with great trouble and used to move his lips (quickly) with the Inspiration." Ibn 'Abbas moved his lips saying, "I am moving my lips in front of you as Allah's Messenger (ﷺ) used to move his." Said moved his lips saying: "I am moving my lips, as I saw Ibn 'Abbas moving his." Ibn 'Abbas added, "So Allah revealed 'Move not your tongue concerning (the Qur'an) to make haste therewith. It is for Us to collect it and to give you (O Muhammad) the ability to recite it (the Quran)' (75.16-17) which means that Allah will make him (the Prophet) remember the portion of the Qur'an which was revealed at that time by heart and recite it. The statement of Allah: 'And when we have recited it to you (O Muhammad through Gabriel) then you follow its (Quran) recital' (75.18) means 'listen to it and be silent.' Then it is for Us (Allah) to make it clear to you' (75.19) means 'Then it is (for Allah) to make you recite it (and its meaning will be clear by itself through your tongue). Afterwards, Allah's Messenger (ﷺ) used to listen to Gabriel whenever he came and after his departure he used to recite it as Gabriel had recited it."
<p></b></div>
<div class=clear></div></div></div><div class="arabic_hadith_full arabic"><span class="arabic_sanad arabic"></span>
<span class="arabic_text_details arabic">حَدَّثَنَا مُوسَى بْنُ إِسْمَاعِيلَ، قَالَ حَدَّثَنَا أَبُو عَوَانَةَ، قَالَ حَدَّثَنَا مُوسَى بْنُ أَبِي عَائِشَةَ، قَالَ حَدَّثَنَا سَعِيدُ بْنُ جُبَيْرٍ، عَنِ ابْنِ عَبَّاسٍ، فِي قَوْلِهِ تَعَالَى ‏<A id="q5" name="q5" href="javascript:openquran(74,16,16)"><c_q5>{‏لاَ تُحَرِّكْ بِهِ لِسَانَكَ لِتَعْجَلَ بِهِ‏}</c_q5></a>‏ قَالَ كَانَ رَسُولُ اللَّهِ صلى الله عليه وسلم يُعَالِجُ مِنَ التَّنْزِيلِ شِدَّةً، وَكَانَ مِمَّا يُحَرِّكُ شَفَتَيْهِ ـ فَقَالَ ابْنُ عَبَّاسٍ فَأَنَا أُحَرِّكُهُمَا لَكُمْ كَمَا كَانَ رَسُولُ اللَّهِ صلى الله عليه وسلم يُحَرِّكُهُمَا‏.‏ وَقَالَ سَعِيدٌ أَنَا أُحَرِّكُهُمَا كَمَا رَأَيْتُ ابْنَ عَبَّاسٍ يُحَرِّكُهُمَا‏.‏ فَحَرَّكَ شَفَتَيْهِ ـ فَأَنْزَلَ اللَّهُ تَعَالَى <A id="q6" name="q6" href="javascript:openquran(74,16,17)"><c_q6>‏{‏لاَ تُحَرِّكْ بِهِ لِسَانَكَ لِتَعْجَلَ بِهِ* إِنَّ عَلَيْنَا جَمْعَهُ وَقُرْآنَهُ‏}‏</c_q6></a> قَالَ جَمْعُهُ لَهُ فِي صَدْرِكَ، وَتَقْرَأَهُ ‏<A id="q7" name="q7" href="javascript:openquran(74,18,18)"><c_q7>{‏فَإِذَا قَرَأْنَاهُ فَاتَّبِعْ قُرْآنَهُ‏}</c_q7></a>‏ قَالَ فَاسْتَمِعْ لَهُ وَأَنْصِتْ ‏<A id="q8" name="q8" href="javascript:openquran(74,19,19)"><c_q8>{‏ثُمَّ إِنَّ عَلَيْنَا بَيَانَهُ‏}</c_q8></a>‏ ثُمَّ إِنَّ عَلَيْنَا أَنْ تَقْرَأَهُ‏.‏ فَكَانَ رَسُولُ اللَّهِ صلى الله عليه وسلم بَعْدَ ذَلِكَ إِذَا أَتَاهُ جِبْرِيلُ اسْتَمَعَ، فَإِذَا انْطَلَقَ جِبْرِيلُ قَرَأَهُ النَّبِيُّ صلى الله عليه وسلم كَمَا قَرَأَهُ‏.‏</span><span class="arabic_sanad arabic"></span></div>
</div>
<!-- End hadith -->

<div class="clear"></div><div class=bottomItems>
<table class=hadith_reference cellspacing=0 cellpadding=0><tr><td><b>Reference</b></td><td>&nbsp;:&nbsp;<a href="/bukhari:5">Sahih al-Bukhari 5</a></td></tr><tr><td>In-book reference</td><td>&nbsp;:&nbsp;Book 1, Hadith 5</td></tr><tr><td><span class="deprecated_reference">USC-MSA web (English) reference</span></td><td>&nbsp;: <span class="deprecated_reference">Vol. 1, Book 1, Hadith 4</span></td></tr> <tr><td>&nbsp;&nbsp;<span class="deprecated_reference"><i>(deprecated numbering scheme)</i></span></td></tr></table><div class="hadith_permalink"><span class=reportlink href="javascript: void(0);" onclick="reportHadith(40, 'h100050')">Report Error</span> | <span class=sharelink onclick="share('/bukhari:5')">Share</span> | <span class=copylink title="Copy hadith to clipboard">Copy</span> <span class=copycbcaret title="Change copy options">▼</span></div></div><div class=clear></div></div><!-- end actual hadith container --><div class=clear></div><a name=C5.00></a>
<div class=chapter>
<div class=echapno>(5)</div><div class=englishchapter>Chapter: </div>
<div class=achapno>(5)</div>
<div class="arabicchapter arabic">باب </div><div class=clear></div>
</div>
<div class=clear></div>
<div class="actualHadithContainer hadith_container_bukhari" id=h100060>
<!-- Begin hadith -->

<a name=6></a>
<div class="hadith_reference_sticky">Sahih al-Bukhari 6</div><div class="hadithTextContainers" id=htc100060><div class="englishcontainer" id=t100060><div class="english_hadith_full"><div class=hadith_narrated><p>

     Narrated Ibn 'Abbas:</div><div class=text_details><p>

     Allah's Messenger (ﷺ) was the most generous of all the people, and he used 
     to reach the peak in generosity in the month of Ramadan when Gabriel 
     met him. Gabriel used to meet him every night of Ramadan to teach him 
     the Qur'an. Allah's Messenger (ﷺ) was the most generous person, even more 
     generous than the strong uncontrollable wind (in readiness and haste 
     to do charitable deeds).
<p></b></div>
<div class=clear></div></div></div><div class="arabic_hadith_full arabic"><span class="arabic_sanad arabic"></span>
<span class="arabic_text_details arabic">حَدَّثَنَا عَبْدَانُ، قَالَ أَخْبَرَنَا عَبْدُ اللَّهِ، قَالَ أَخْبَرَنَا يُونُسُ، عَنِ الزُّهْرِيِّ، ح وَحَدَّثَنَا بِشْرُ بْنُ مُحَمَّدٍ، قَالَ أَخْبَرَنَا عَبْدُ اللَّهِ، قَالَ أَخْبَرَنَا يُونُسُ، وَمَعْمَرٌ، عَنِ الزُّهْرِيِّ، نَحْوَهُ قَالَ أَخْبَرَنِي عُبَيْدُ اللَّهِ بْنُ عَبْدِ اللَّهِ، عَنِ ابْنِ عَبَّاسٍ، قَالَ كَانَ رَسُولُ اللَّهِ صلى الله عليه وسلم أَجْوَدَ النَّاسِ، وَكَانَ أَجْوَدُ مَا يَكُونُ فِي رَمَضَانَ حِينَ يَلْقَاهُ جِبْرِيلُ، وَكَانَ يَلْقَاهُ فِي كُلِّ لَيْلَةٍ مِنْ رَمَضَانَ فَيُدَارِسُهُ الْقُرْآنَ، فَلَرَسُولُ اللَّهِ صلى الله عليه وسلم أَجْوَدُ بِالْخَيْرِ مِنَ الرِّيحِ الْمُرْسَلَةِ‏.‏</span><span class="arabic_sanad arabic"></span></div>
</div>
<!-- End hadith -->

<div class="clear"></div><div class=bottomItems>
<table class=hadith_reference cellspacing=0 cellpadding=0><tr><td><b>Reference</b></td><td>&nbsp;:&nbsp;<a href="/bukhari:6">Sahih al-Bukhari 6</a></td></tr><tr><td>In-book reference</td><td>&nbsp;:&nbsp;Book 1, Hadith 6</td></tr><tr><td><span class="deprecated_reference">USC-MSA web (English) reference</span></td><td>&nbsp;: <span class="deprecated_reference">Vol. 1, Book 1, Hadith 5</span></td></tr> <tr><td>&nbsp;&nbsp;<span class="deprecated_reference"><i>(deprecated numbering scheme)</i></span></td></tr></table><div class="hadith_permalink"><span class=reportlink href="javascript: void(0);" onclick="reportHadith(50, 'h100060')">Report Error</span> | <span class=sharelink onclick="share('/bukhari:6')">Share</span> | <span class=copylink title="Copy hadith to clipboard">Copy</span> <span class=copycbcaret title="Change copy options">▼</span></div></div><div class=clear></div></div><!-- end actual hadith container --><div class=clear></div><a name=C6.00></a>
<div class=chapter>
<div class=echapno>(6)</div><div class=englishchapter>Chapter: </div>
<div class=achapno>(6)</div>
<div class="arabicchapter arabic">باب </div><div class=clear></div>
</div>
<div class=clear></div>
<div class="actualHadithContainer hadith_container_bukhari" id=h100070>
<!-- Begin hadith -->

<a name=7></a>
<div class="hadith_reference_sticky">Sahih al-Bukhari 7</div><div class="hadithTextContainers" id=htc100070><div class="englishcontainer" id=t100070><div class="english_hadith_full"><div class=hadith_narrated><p>

     Narrated 'Abdullah bin 'Abbas:</div><div class=text_details><p>

     Abu Sufyan bin Harb informed me that Heraclius had sent a messenger to
     him while he had been accompanying a caravan from Quraish. They were 
     merchants doing business in Sham (Syria, Palestine, Lebanon and 
     Jordan), at the time when Allah's Messenger (ﷺ) had truce with Abu Sufyan 
     and Quraish infidels. So Abu Sufyan and his companions went to 
     Heraclius at Ilya (Jerusalem). Heraclius called them in the court and 
     he had all the senior Roman dignitaries around him. He called for his 
     translator who, translating Heraclius's question said to them, "Who 
     amongst you is closely related to that man who claims to be a 
     Prophet?" Abu Sufyan replied, "I am the nearest relative to him 
     (amongst the group)."
<p>

     Heraclius said, "Bring him (Abu Sufyan) close to me and make his 
     companions stand behind him." Abu Sufyan added, Heraclius told his 
     translator to tell my companions that he wanted to put some questions 
     to me regarding that man (The Prophet) and that if I told a lie they 
     (my companions) should contradict me." Abu Sufyan added, "By Allah! 
     Had I not been afraid of my companions labeling me a liar, I would not
     have spoken the truth about the Prophet. The first question he asked 
     me about him was:
<p>

     'What is his family status amongst you?' 
<p>

     I replied, 'He belongs to a good (noble) family amongst us.' 
<p>

     Heraclius further asked, 'Has anybody amongst you ever claimed the 
     same (i.e. to be a Prophet) before him?'
<p>

     I replied, 'No.'
<p>

     He said, 'Was anybody amongst his ancestors a king?'
<p>

     I replied, 'No.'
<p>

     Heraclius asked, 'Do the nobles or the poor follow him?'
<p>

     I replied, 'It is the poor who follow him.'
<p>

     He said, 'Are his followers increasing decreasing (day by day)?'
<p>

     I replied, 'They are increasing.'
<p>

     He then asked, 'Does anybody amongst those who embrace his religion 
     become displeased and renounce the religion afterwards?'
<p>

     I replied, 'No.'
<p>

     Heraclius said, 'Have you ever accused him of telling lies before his 
     claim (to be a Prophet)?'
<p>

     I replied, 'No. '
<p>

     Heraclius said, 'Does he break his promises?'
<p>

     I replied, 'No. We are at truce with him but we do not know what he 
     will do in it.' I could not find opportunity to say anything against 
     him except that.
<p>

     Heraclius asked, 'Have you ever had a war with him?'
<p>

     I replied, 'Yes.'
<p>

     Then he said, 'What was the outcome of the battles?'
<p>

     I replied, 'Sometimes he was victorious and sometimes we.'
<p>

     Heraclius said, 'What does he order you to do?'
<p>

     I said, 'He tells us to worship Allah and Allah alone and not to 
     worship anything along with Him, and to renounce all that our 
     ancestors had said. He orders us to pray, to speak the truth, to be 
     chaste and to keep good relations with our Kith and kin.'
<p>

     Heraclius asked the translator to convey to me the following, I asked 
     you about his family and your reply was that he belonged to a very 
     noble family. In fact all the Apostles come from noble families 
     amongst their respective peoples. I questioned you whether anybody 
     else amongst you claimed such a thing, your reply was in the negative.
     If the answer had been in the affirmative, I would have thought that 
     this man was following the previous man's statement. Then I asked you 
     whether anyone of his ancestors was a king. Your reply was in the 
     negative, and if it had been in the affirmative, I would have thought 
     that this man wanted to take back his ancestral kingdom.
<p>

     I further asked whether he was ever accused of telling lies before he 
     said what he said, and your reply was in the negative. So I wondered 
     how a person who does not tell a lie about others could ever tell a 
     lie about Allah. I, then asked you whether the rich people followed 
     him or the poor. You replied that it was the poor who followed him. 
     And in fact all the Apostle have been followed by this very class of 
     people. Then I asked you whether his followers were increasing or 
     decreasing. You replied that they were increasing, and in fact this is
     the way of true faith, till it is complete in all respects. I further 
     asked you whether there was anybody, who, after embracing his 
     religion, became displeased and discarded his religion. Your reply was
     in the negative, and in fact this is (the sign of) true faith, when 
     its delight enters the hearts and mixes with them completely. I asked 
     you whether he had ever betrayed. You replied in the negative and 
     likewise the Apostles never betray. Then I asked you what he ordered 
     you to do. You replied that he ordered you to worship Allah and Allah 
     alone and not to worship any thing along with Him and forbade you to 
     worship idols and ordered you to pray, to speak the truth and to be 
     chaste. If what you have said is true, he will very soon occupy this 
     place underneath my feet and I knew it (from the scriptures) that he 
     was going to appear but I did not know that he would be from you, and 
     if I could reach him definitely, I would go immediately to meet him 
     and if I were with him, I would certainly wash his feet.' Heraclius 
     then asked for the letter addressed by Allah's Apostle
<p>

     which was delivered by Dihya to the Governor of Busra, who forwarded 
     it to Heraclius to read. The contents of the letter were as follows: 
     "In the name of Allah the Beneficent, the Merciful (This letter is) 
     from Muhammad the slave of Allah and His Apostle to Heraclius the 
     ruler of Byzantine. Peace be upon him, who follows the right path. 
     Furthermore I invite you to Islam, and if you become a Muslim you will
     be safe, and Allah will double your reward, and if you reject this 
     invitation of Islam you will be committing a sin of
     Arisiyin (tillers, farmers i.e. your people). And  (Allah's Statement:)
<p>

     'O people of the scripture! Come to a word common to you and us that 
     we worship none but Allah and that we associate nothing in worship 
     with Him, and that none of us shall take others as Lords beside Allah.
     Then, if they turn away, say: Bear witness that we are Muslims (those 
     who have surrendered to Allah).' (3:64).
<p>

     Abu Sufyan then added, "When Heraclius had finished his speech and had
     read the letter, there was a great hue and cry in the Royal Court. So 
     we were turned out of the court. I told my companions that the 
     question of Ibn-Abi-Kabsha) (the Prophet (ﷺ) Muhammad) has become so 
     prominent that even the King of Bani Al-Asfar (Byzantine) is afraid of
     him. Then I started to become sure that he (the Prophet) would be the 
     conqueror in the near future till I embraced Islam (i.e. Allah guided 
     me to it)."
<p>

     The sub narrator adds, "Ibn An-Natur was the Governor of llya' 
     (Jerusalem) and Heraclius was the head of the Christians of Sham. Ibn 
     An-Natur narrates that once while Heraclius was visiting ilya' 
     (Jerusalem), he got up in the morning with a sad mood. Some of his 
     priests asked him why he was in that mood? Heraclius was a foreteller 
     and an astrologer. He replied, 'At night when I looked at the stars, I
     saw that the leader of those who practice circumcision had appeared 
     (become the conqueror). Who are they who practice circumcision?' The 
     people replied, 'Except the Jews nobody practices circumcision, so you
     should not be afraid of them (Jews).
<p>

     'Just Issue orders to kill every Jew present in the country.'
<p>

     While they were discussing it, a messenger sent by the king of Ghassan
     to convey the news of Allah's Messenger (ﷺ) to Heraclius was brought in. 
     Having heard the news, he (Heraclius) ordered the people to go and see
     whether the messenger of Ghassan was circumcised. The people, after 
     seeing him, told Heraclius that he was circumcised. Heraclius then 
     asked him about the Arabs. The messenger replied, 'Arabs also practice
     circumcision.'
<p>

     (After hearing that) Heraclius remarked that sovereignty of the 'Arabs
     had appeared. Heraclius then wrote a letter to his friend in Rome who 
     was as good as Heraclius in knowledge. Heraclius then left for Homs. 
     (a town in Syrian and stayed there till he received the reply of his 
     letter from his friend who agreed with him in his opinion about the 
     emergence of the Prophet (ﷺ) and the fact that he was a Prophet. On that 
     Heraclius invited all the heads of the Byzantines to assemble in his 
     palace at Homs. When they assembled, he ordered that all the doors of 
     his palace be closed. Then he came out and said, 'O Byzantines! If 
     success is your desire and if you seek right guidance and want your 
     empire to remain then give a pledge of allegiance to this Prophet 
     (i.e. embrace Islam).'
<p>

     (On hearing the views of Heraclius) the people ran towards the gates 
     of the palace like onagers but found the doors closed. Heraclius 
     realized their hatred towards Islam and when he lost the hope of their
     embracing Islam, he ordered that they should be brought back in 
     audience.
<p>

     (When they returned) he said, 'What already said was just to test the 
     strength of your conviction and I have seen it.' The people prostrated
     before him and became pleased with him, and this was the end of 
     Heraclius's story (in connection with his faith).
<p></b></div>
<div class=clear></div></div></div><div class="arabic_hadith_full arabic"><span class="arabic_sanad arabic"></span>
<span class="arabic_text_details arabic">حَدَّثَنَا أَبُو الْيَمَانِ الْحَكَمُ بْنُ نَافِعٍ، قَالَ أَخْبَرَنَا شُعَيْبٌ، عَنِ الزُّهْرِيِّ، قَالَ أَخْبَرَنِي عُبَيْدُ اللَّهِ بْنُ عَبْدِ اللَّهِ بْنِ عُتْبَةَ بْنِ مَسْعُودٍ، أَنَّ عَبْدَ اللَّهِ بْنَ عَبَّاسٍ، أَخْبَرَهُ أَنَّ أَبَا سُفْيَانَ بْنَ حَرْبٍ أَخْبَرَهُ أَنَّ هِرَقْلَ أَرْسَلَ إِلَيْهِ فِي رَكْبٍ مِنْ قُرَيْشٍ ـ وَكَانُوا تُجَّارًا بِالشَّأْمِ ـ فِي الْمُدَّةِ الَّتِي كَانَ رَسُولُ اللَّهِ صلى الله عليه وسلم مَادَّ فِيهَا أَبَا سُفْيَانَ وَكُفَّارَ قُرَيْشٍ، فَأَتَوْهُ وَهُمْ بِإِيلِيَاءَ فَدَعَاهُمْ فِي مَجْلِسِهِ، وَحَوْلَهُ عُظَمَاءُ الرُّومِ ثُمَّ دَعَاهُمْ وَدَعَا بِتَرْجُمَانِهِ فَقَالَ أَيُّكُمْ أَقْرَبُ نَسَبًا بِهَذَا الرَّجُلِ الَّذِي يَزْعُمُ أَنَّهُ نَبِيٌّ فَقَالَ أَبُو سُفْيَانَ فَقُلْتُ أَنَا أَقْرَبُهُمْ نَسَبًا‏.‏ فَقَالَ أَدْنُوهُ مِنِّي، وَقَرِّبُوا أَصْحَابَهُ، فَاجْعَلُوهُمْ عِنْدَ ظَهْرِهِ‏.‏ ثُمَّ قَالَ لِتَرْجُمَانِهِ قُلْ لَهُمْ إِنِّي سَائِلٌ هَذَا عَنْ هَذَا الرَّجُلِ، فَإِنْ كَذَبَنِي فَكَذِّبُوهُ‏.‏ فَوَاللَّهِ لَوْلاَ الْحَيَاءُ مِنْ أَنْ يَأْثِرُوا عَلَىَّ كَذِبًا لَكَذَبْتُ عَنْهُ، ثُمَّ كَانَ أَوَّلَ مَا سَأَلَنِي عَنْهُ أَنْ قَالَ كَيْفَ نَسَبُهُ فِيكُمْ قُلْتُ هُوَ فِينَا ذُو نَسَبٍ‏.‏ قَالَ فَهَلْ قَالَ هَذَا الْقَوْلَ مِنْكُمْ أَحَدٌ قَطُّ قَبْلَهُ قُلْتُ لاَ‏.‏ قَالَ فَهَلْ كَانَ مِنْ آبَائِهِ مِنْ مَلِكٍ قُلْتُ لاَ‏.‏ قَالَ فَأَشْرَافُ النَّاسِ يَتَّبِعُونَهُ أَمْ ضُعَفَاؤُهُمْ فَقُلْتُ بَلْ ضُعَفَاؤُهُمْ‏.‏ قَالَ أَيَزِيدُونَ أَمْ يَنْقُصُونَ قُلْتُ بَلْ يَزِيدُونَ‏.‏ قَالَ فَهَلْ يَرْتَدُّ أَحَدٌ مِنْهُمْ سَخْطَةً لِدِينِهِ بَعْدَ أَنْ يَدْخُلَ فِيهِ قُلْتُ لاَ‏.‏ قَالَ فَهَلْ كُنْتُمْ تَتَّهِمُونَهُ بِالْكَذِبِ قَبْلَ أَنْ يَقُولَ مَا قَالَ قُلْتُ لاَ‏.‏ قَالَ فَهَلْ يَغْدِرُ قُلْتُ لاَ، وَنَحْنُ مِنْهُ فِي مُدَّةٍ لاَ نَدْرِي مَا هُوَ فَاعِلٌ فِيهَا‏.‏ قَالَ وَلَمْ تُمْكِنِّي كَلِمَةٌ أُدْخِلُ فِيهَا شَيْئًا غَيْرُ هَذِهِ الْكَلِمَةِ‏.‏ قَالَ فَهَلْ قَاتَلْتُمُوهُ قُلْتُ نَعَمْ‏.‏ قَالَ فَكَيْفَ كَانَ قِتَالُكُمْ إِيَّاهُ قُلْتُ الْحَرْبُ بَيْنَنَا وَبَيْنَهُ سِجَالٌ، يَنَالُ مِنَّا وَنَنَالُ مِنْهُ‏.‏ قَالَ مَاذَا يَأْمُرُكُمْ قُلْتُ يَقُولُ اعْبُدُوا اللَّهَ وَحْدَهُ، وَلاَ تُشْرِكُوا بِهِ شَيْئًا، وَاتْرُكُوا مَا يَقُولُ آبَاؤُكُمْ، وَيَأْمُرُنَا بِالصَّلاَةِ وَالصِّدْقِ وَالْعَفَافِ وَالصِّلَةِ‏.‏ فَقَالَ لِلتَّرْجُمَانِ قُلْ لَهُ سَأَلْتُكَ عَنْ نَسَبِهِ، فَذَكَرْتَ أَنَّهُ فِيكُمْ ذُو نَسَبٍ، فَكَذَلِكَ الرُّسُلُ تُبْعَثُ فِي نَسَبِ قَوْمِهَا، وَسَأَلْتُكَ هَلْ قَالَ أَحَدٌ مِنْكُمْ هَذَا الْقَوْلَ فَذَكَرْتَ أَنْ لاَ، فَقُلْتُ لَوْ كَانَ أَحَدٌ قَالَ هَذَا الْقَوْلَ قَبْلَهُ لَقُلْتُ رَجُلٌ يَأْتَسِي بِقَوْلٍ قِيلَ قَبْلَهُ، وَسَأَلْتُكَ هَلْ كَانَ مِنْ آبَائِهِ مِنْ مَلِكٍ فَذَكَرْتَ أَنْ لاَ، قُلْتُ فَلَوْ كَانَ مِنْ آبَائِهِ مِنْ مَلِكٍ قُلْتُ رَجُلٌ يَطْلُبُ مُلْكَ أَبِيهِ، وَسَأَلْتُكَ هَلْ كُنْتُمْ تَتَّهِمُونَهُ بِالْكَذِبِ قَبْلَ أَنْ يَقُولَ مَا قَالَ فَذَكَرْتَ أَنْ لاَ، فَقَدْ أَعْرِفُ أَنَّهُ لَمْ يَكُنْ لِيَذَرَ الْكَذِبَ عَلَى النَّاسِ وَيَكْذِبَ عَلَى اللَّهِ، وَسَأَلْتُكَ أَشْرَافُ النَّاسِ اتَّبَعُوهُ أَمْ ضُعَفَاؤُهُمْ فَذَكَرْتَ أَنَّ ضُعَفَاءَهُمُ اتَّبَعُوهُ، وَهُمْ أَتْبَاعُ الرُّسُلِ، وَسَأَلْتُكَ أَيَزِيدُونَ أَمْ يَنْقُصُونَ فَذَكَرْتَ أَنَّهُمْ يَزِيدُونَ، وَكَذَلِكَ أَمْرُ الإِيمَانِ حَتَّى يَتِمَّ، وَسَأَلْتُكَ أَيَرْتَدُّ أَحَدٌ سَخْطَةً لِدِينِهِ بَعْدَ أَنْ يَدْخُلَ فِيهِ فَذَكَرْتَ أَنْ لاَ، وَكَذَلِكَ الإِيمَانُ حِينَ تُخَالِطُ بَشَاشَتُهُ الْقُلُوبَ، وَسَأَلْتُكَ هَلْ يَغْدِرُ فَذَكَرْتَ أَنْ لاَ، وَكَذَلِكَ الرُّسُلُ لاَ تَغْدِرُ، وَسَأَلْتُكَ بِمَا يَأْمُرُكُمْ، فَذَكَرْتَ أَنَّهُ يَأْمُرُكُمْ أَنْ تَعْبُدُوا اللَّهَ، وَلاَ تُشْرِكُوا بِهِ شَيْئًا، وَيَنْهَاكُمْ عَنْ عِبَادَةِ الأَوْثَانِ، وَيَأْمُرُكُمْ بِالصَّلاَةِ وَالصِّدْقِ وَالْعَفَافِ‏.‏ فَإِنْ كَانَ مَا تَقُولُ حَقًّا فَسَيَمْلِكُ مَوْضِعَ قَدَمَىَّ هَاتَيْنِ، وَقَدْ كُنْتُ أَعْلَمُ أَنَّهُ خَارِجٌ، لَمْ أَكُنْ أَظُنُّ أَنَّهُ مِنْكُمْ، فَلَوْ أَنِّي أَعْلَمُ أَنِّي أَخْلُصُ إِلَيْهِ لَتَجَشَّمْتُ لِقَاءَهُ، وَلَوْ كُنْتُ عِنْدَهُ لَغَسَلْتُ عَنْ قَدَمِهِ‏.‏ ثُمَّ دَعَا بِكِتَابِ رَسُولِ اللَّهِ صلى الله عليه وسلم الَّذِي بَعَثَ بِهِ دِحْيَةُ إِلَى عَظِيمِ بُصْرَى، فَدَفَعَهُ إِلَى هِرَقْلَ فَقَرَأَهُ فَإِذَا فِيهِ بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيمِ‏.‏ مِنْ مُحَمَّدٍ عَبْدِ اللَّهِ وَرَسُولِهِ إِلَى هِرَقْلَ عَظِيمِ الرُّومِ‏.‏ سَلاَمٌ عَلَى مَنِ اتَّبَعَ الْهُدَى، أَمَّا بَعْدُ فَإِنِّي أَدْعُوكَ بِدِعَايَةِ الإِسْلاَمِ، أَسْلِمْ تَسْلَمْ، يُؤْتِكَ اللَّهُ أَجْرَكَ مَرَّتَيْنِ، فَإِنْ تَوَلَّيْتَ فَإِنَّ عَلَيْكَ إِثْمَ الأَرِيسِيِّينَ وَ‏{‏يَا أَهْلَ الْكِتَابِ تَعَالَوْا إِلَى كَلِمَةٍ سَوَاءٍ بَيْنَنَا وَبَيْنَكُمْ أَنْ لاَ نَعْبُدَ إِلاَّ اللَّهَ وَلاَ نُشْرِكَ بِهِ شَيْئًا وَلاَ يَتَّخِذَ بَعْضُنَا بَعْضًا أَرْبَابًا مِنْ دُونِ اللَّهِ فَإِنْ تَوَلَّوْا فَقُولُوا اشْهَدُوا بِأَنَّا مُسْلِمُونَ‏}‏ قَالَ أَبُو سُفْيَانَ فَلَمَّا قَالَ مَا قَالَ، وَفَرَغَ مِنْ قِرَاءَةِ الْكِتَابِ كَثُرَ عِنْدَهُ الصَّخَبُ، وَارْتَفَعَتِ الأَصْوَاتُ وَأُخْرِجْنَا، فَقُلْتُ لأَصْحَابِي حِينَ أُخْرِجْنَا لَقَدْ أَمِرَ أَمْرُ ابْنِ أَبِي كَبْشَةَ، إِنَّهُ يَخَافُهُ مَلِكُ بَنِي الأَصْفَرِ‏.‏ فَمَا زِلْتُ مُوقِنًا أَنَّهُ سَيَظْهَرُ حَتَّى أَدْخَلَ اللَّهُ عَلَىَّ الإِسْلاَمَ‏.‏ وَكَانَ ابْنُ النَّاظُورِ صَاحِبُ إِيلِيَاءَ وَهِرَقْلَ سُقُفًّا عَلَى نَصَارَى الشَّأْمِ، يُحَدِّثُ أَنَّ هِرَقْلَ حِينَ قَدِمَ إِيلِيَاءَ أَصْبَحَ يَوْمًا خَبِيثَ النَّفْسِ، فَقَالَ بَعْضُ بَطَارِقَتِهِ قَدِ اسْتَنْكَرْنَا هَيْئَتَكَ‏.‏ قَالَ ابْنُ النَّاظُورِ وَكَانَ هِرَقْلُ حَزَّاءً يَنْظُرُ فِي النُّجُومِ، فَقَالَ لَهُمْ حِينَ سَأَلُوهُ إِنِّي رَأَيْتُ اللَّيْلَةَ حِينَ نَظَرْتُ فِي النُّجُومِ مَلِكَ الْخِتَانِ قَدْ ظَهَرَ، فَمَنْ يَخْتَتِنُ مِنْ هَذِهِ الأُمَّةِ قَالُوا لَيْسَ يَخْتَتِنُ إِلاَّ الْيَهُودُ فَلاَ يُهِمَّنَّكَ شَأْنُهُمْ وَاكْتُبْ إِلَى مَدَايِنِ مُلْكِكَ، فَيَقْتُلُوا مَنْ فِيهِمْ مِنَ الْيَهُودِ‏.‏ فَبَيْنَمَا هُمْ عَلَى أَمْرِهِمْ أُتِيَ هِرَقْلُ بِرَجُلٍ أَرْسَلَ بِهِ مَلِكُ غَسَّانَ، يُخْبِرُ عَنْ خَبَرِ رَسُولِ اللَّهِ صلى الله عليه وسلم فَلَمَّا اسْتَخْبَرَهُ هِرَقْلُ قَالَ اذْهَبُوا فَانْظُرُوا أَمُخْتَتِنٌ هُوَ أَمْ لاَ‏.‏ فَنَظَرُوا إِلَيْهِ، فَحَدَّثُوهُ أَنَّهُ مُخْتَتِنٌ، وَسَأَلَهُ عَنِ الْعَرَبِ فَقَالَ هُمْ يَخْتَتِنُونَ‏.‏ فَقَالَ هِرَقْلُ هَذَا مَلِكُ هَذِهِ الأُمَّةِ قَدْ ظَهَرَ‏.‏ ثُمَّ كَتَبَ هِرَقْلُ إِلَى صَاحِبٍ لَهُ بِرُومِيَةَ، وَكَانَ نَظِيرَهُ فِي الْعِلْمِ، وَسَارَ هِرَقْلُ إِلَى حِمْصَ، فَلَمْ يَرِمْ حِمْصَ حَتَّى أَتَاهُ كِتَابٌ مِنْ صَاحِبِهِ يُوَافِقُ رَأْىَ هِرَقْلَ عَلَى خُرُوجِ النَّبِيِّ صلى الله عليه وسلم وَأَنَّهُ نَبِيٌّ، فَأَذِنَ هِرَقْلُ لِعُظَمَاءِ الرُّومِ فِي دَسْكَرَةٍ لَهُ بِحِمْصَ ثُمَّ أَمَرَ بِأَبْوَابِهَا فَغُلِّقَتْ، ثُمَّ اطَّلَعَ فَقَالَ يَا مَعْشَرَ الرُّومِ، هَلْ لَكُمْ فِي الْفَلاَحِ وَالرُّشْدِ وَأَنْ يَثْبُتَ مُلْكُكُمْ فَتُبَايِعُوا هَذَا النَّبِيَّ، فَحَاصُوا حَيْصَةَ حُمُرِ الْوَحْشِ إِلَى الأَبْوَابِ، فَوَجَدُوهَا قَدْ غُلِّقَتْ، فَلَمَّا رَأَى هِرَقْلُ نَفْرَتَهُمْ، وَأَيِسَ مِنَ الإِيمَانِ قَالَ رُدُّوهُمْ عَلَىَّ‏.‏ وَقَالَ إِنِّي قُلْتُ مَقَالَتِي آنِفًا أَخْتَبِرُ بِهَا شِدَّتَكُمْ عَلَى دِينِكُمْ، فَقَدْ رَأَيْتُ‏.‏ فَسَجَدُوا لَهُ وَرَضُوا عَنْهُ، فَكَانَ ذَلِكَ آخِرَ شَأْنِ هِرَقْلَ‏.‏ رَوَاهُ صَالِحُ بْنُ كَيْسَانَ وَيُونُسُ وَمَعْمَرٌ عَنِ الزُّهْرِيِّ‏.‏</span><span class="arabic_sanad arabic"></span></div>
</div>
<!-- End hadith -->

<div class="clear"></div><div class=bottomItems>
<table class=hadith_reference cellspacing=0 cellpadding=0><tr><td><b>Reference</b></td><td>&nbsp;:&nbsp;<a href="/bukhari:7">Sahih al-Bukhari 7</a></td></tr><tr><td>In-book reference</td><td>&nbsp;:&nbsp;Book 1, Hadith 7</td></tr><tr><td><span class="deprecated_reference">USC-MSA web (English) reference</span></td><td>&nbsp;: <span class="deprecated_reference">Vol. 1, Book 1, Hadith 6</span></td></tr> <tr><td>&nbsp;&nbsp;<span class="deprecated_reference"><i>(deprecated numbering scheme)</i></span></td></tr></table><div class="hadith_permalink"><span class=reportlink href="javascript: void(0);" onclick="reportHadith(60, 'h100070')">Report Error</span> | <span class=sharelink onclick="share('/bukhari:7')">Share</span> | <span class=copylink title="Copy hadith to clipboard">Copy</span> <span class=copycbcaret title="Change copy options">▼</span></div></div><div class=clear></div></div><!-- end actual hadith container --><div class=clear></div><!-- <div align=right><i>Content on this page was last updated on </i></div> --></div>	
	<script>
		(function () {

			var hCount = $(".chapter").length;
			var hExpectedCount = 6			
			if ( hCount != hExpectedCount ) {
				var message = "\n" + location.pathname.substring(1) + "\tshown: " + hCount + "\texpected: " + hExpectedCount;

				$.ajax({
					type : "POST",
					url : "/ajax/log/hadithcount",
					data: {msg: message, _csrf_frontend:'rMdZKLs2qXmobj_iGi_375317yuWo3bGsOXujGr8jzTFhDpO60LDDcYZT7siTa6l2cSsSeSaOq6FtbTOIovGeA=='},
				});
			}
		})();
	</script>

	

	<div class="clear"></div>
    </div><!-- main close -->
	</div> <!-- mainContainer close -->
	<a href="#"><div id=back-to-top></div></a>
	<div class="clear"></div>
	</div> <!-- nonheader close -->
    
<div class=footer>
	<a href="/about">About</a> |
	<a href="/news">News</a> |
	<a href="/support">Support</a> |
	<a href="/developers">Developers</a> |
    <a href="/contact">Contact</a>
	<div class="sm_links">
		<a href="https://www.facebook.com/Sunnahcom-104172848076350" target="_blank"><i class="icn-fb"></i></a>
		<a href="https://www.instagram.com/_sunnahcom/" target="_blank"><i class="icn-ig"></i></a>
		<a href="https://twitter.com/SunnahCom" target="_blank"><i class="icn-twitter"></i></a>
	</div>
<div class=clear></div>
</div>


<script type="text/javascript">
var sc_project=7148282;
var sc_invisible=1;
var sc_security="63a57073";
</script>
<link href="/css/fonts/fontello/css/icn-font.css?ver=1608065995" rel="stylesheet" type="text/css" />
<script type="text/javascript" src="https://www.statcounter.com/counter/counter.js" async></script>
<noscript>
<div class="statcounter"><a title="Web Analytics" href="https://statcounter.com/" target="_blank">
<img class="statcounter" src="https://c.statcounter.com/7148282/0/63a57073/1/" alt="Web Analytics"></a>
</div>
</noscript>

    <div  id="cb_flyout" onchange="saveCbSettings()" style="display: none">
	<fieldset>
		<legend>Hadith Text</legend>
			<label title="The Arabic text of the Hadith.">
				<input type="checkbox" name="arabic" value="arabic">Arabic</label>
			<label title="The translation that is displaying on page.">
				<input type="checkbox" name="translation" value="translation">Translation</label>		
			<label title="The authenticity grade of the Hadith, if available.">
				<input type="checkbox" name="grade" value="grade">Grade</label>
	</fieldset>

	<fieldset>
		<legend>Reference</legend>
			<label title="The reference will only contain the collection name and the overall Hadith number.">
				<input type="radio" name="ref" value="concise">Concise</label>
			<label title="The reference will contain more information in English and Arabic, such as the book name/number, chapter name/number, Hadith number within book, etc., whatever is available.">
				<input type="radio" name="ref" value="detailed">Detailed</label>
			<label title="The web link for the Hadith.">
				<input type="checkbox" name="url" value="url">URL</label>
	</fieldset>
</div>	<div class="clear"></div>

</div><!-- site div close -->
</body>
</html>
'''

# Initialize BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# List to hold all hadith data
hadith_list = []

# Find all hadith containers
hadith_containers = soup.find_all('div', class_='actualHadithContainer')

for container in hadith_containers:
    hadith_data = {}
    
    # Extract the English hadith text
    english_container = container.find('div', class_='english_hadith_full')
    if english_container:
        narrator = english_container.find('div', class_='hadith_narrated')
        text_details = english_container.find('div', class_='text_details')
        
        hadith_data['narrator'] = narrator.text.strip() if narrator else None
        hadith_data['english_text'] = text_details.text.strip() if text_details else None
    
    # Extract the Arabic hadith text
    # arabic_container = container.find('div', class_='arabic_hadith_full')
    # if arabic_container:
    #     arabic_text = arabic_container.find('span', class_='arabic_text_details')
    #     hadith_data['arabic_text'] = arabic_text.text.strip() if arabic_text else None

    hadith_link = container.find('td', string=lambda t: t and 'Reference' in t)
    if hadith_link:
        next_td = hadith_link.find_next_sibling('td')
        if next_td:
            link = next_td.find('a')
            if link:
                href = link.get('href')
                hadith_data['hadith_link'] = href
    # Extract hadith reference
    reference = container.find('div', class_='hadith_reference_sticky')
    hadith_data['reference'] = reference.text.strip() if reference else None

    # Add hadith data to the list
    hadith_list.append(hadith_data)

# Convert the list of hadiths to JSON format
hadith_json = json.dumps(hadith_list, ensure_ascii=False, indent=4)

# Output the JSON
# print(hadith_json)

# Save to a JSON file
with open('hadith_data.json', 'w', encoding='utf-8') as f:
    json.dump(hadith_list, f, ensure_ascii=False, indent=4)

print("Data saved to hadith_data.json")
