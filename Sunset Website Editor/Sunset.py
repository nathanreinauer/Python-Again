
import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
from datetime import date
##import os.path
##import shutil
##from bs4 import BeautifulSoup
##import requests

conn = sqlite3.connect('movielist.db')
c = conn.cursor()
##varID = '20'

class GUIhtml:

#-------------------------GUI-------------------------#

    def __init__(self, master):

        # Frame
        master.title('Sunset Movie Editor')
        master.resizable(False,False)
        master.configure(background='#009999')

        # Colors, fonts, etc.
        self.style = ttk.Style()
        self.style.configure('TFrame',background='#009999')
        self.style.configure('TButton',background='#009999')
        self.style.configure('TLabel',background='#009999', font=('Arial',11))
        self.style.configure('Header.TLabel',background='#009999',font=('Arial',18,'bold'))

        # Header
        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        # Header content
        ttk.Label(self.frame_header,text='Movie Editor',style='Header.TLabel',foreground='#ccffff').grid(row=0,column=1,pady=5)

        # Body 
        self.frame_content=ttk.Frame(master)
        self.frame_content.pack()

        # Labels / Text boxes / Placement
        ttk.Label(self.frame_content,text='Title',foreground='#ccffff').grid(row=3,column=0,pady=5, sticky='e')
        self.text_title=Text(self.frame_content,width=65,height=1)
        self.text_title.grid(row=3,column=1,columnspan=3,padx=5, sticky='w')

        ttk.Label(self.frame_content,text='2D Dates',foreground='#ccffff').grid(row=4,column=0,pady=5, sticky='e')
        self.text_date2d=Text(self.frame_content,width=25,height=1)
        self.text_date2d.grid(row=4,column=1,columnspan=1,padx=5, sticky='w')
##        self.text_date2d.insert(END, ' in 2D')

        ttk.Label(self.frame_content,text='3D Dates',foreground='#ccffff').grid(row=4,column=2,pady=5, sticky='e')
        self.text_date3d=Text(self.frame_content,width=25,height=1)
        self.text_date3d.grid(row=4,column=3,columnspan=1,padx=5, sticky='w')
##        self.text_date3d.insert(END, ' in 3D')

        ttk.Label(self.frame_content,text='Cast',foreground='#ccffff').grid(row=5,column=0,pady=5, sticky='e')
        self.text_cast=Text(self.frame_content,width=75,height=4, wrap=WORD)
        self.text_cast.grid(row=5,column=1,columnspan=3,padx=5, sticky='w')

        ttk.Label(self.frame_content,text='Synopsis',foreground='#ccffff').grid(row=6,column=0,pady=5, sticky='e')
        self.text_summary=Text(self.frame_content,width=75,height=9, wrap=WORD)
        self.text_summary.grid(row=6,column=1,columnspan=3,padx=5, sticky='w')

        ttk.Label(self.frame_content,text='Runtime',foreground='#ccffff').grid(row=7,column=0,pady=5, sticky='e')
        self.text_runtime=Text(self.frame_content,width=20,height=1)
        self.text_runtime.grid(row=7,column=1,columnspan=2,padx=5, sticky='w')

        ttk.Label(self.frame_content,text='youtube.com/watch?v=',foreground='#ccffff').grid(row=7,column=2,pady=5, sticky='e')
        self.text_trailer=Text(self.frame_content,width=15,height=1)
        self.text_trailer.grid(row=7,column=3,columnspan=2,padx=5, sticky='w')

        ttk.Label(self.frame_content,text='Image',foreground='#ccffff').grid(row=8,column=0,pady=5, sticky='e')
        self.text_image=Text(self.frame_content,width=30,height=1)
        self.text_image.grid(row=8,column=1,columnspan=1,padx=5, sticky='w')

        ttk.Label(self.frame_content,text='Rating',foreground='#ccffff').grid(row=8,column=2,pady=5, sticky='e')
        self.text_rating=Text(self.frame_content,width=7,height=1)
        self.text_rating.grid(row=8,column=3,columnspan=2,padx=5, sticky='w')

        self.contentBox = StringVar()		 
        self.combobox = ttk.Combobox(self.frame_content, textvariable = self.contentBox, state='readonly', width=30)		  	 
        self.combobox.grid(row=12,column=1)
        self.combobox.config(values = self.forComboBox())
        self.contentBox.set('Select movie:')


    
        # Buttons
        ttk.Button(self.frame_content,text='Update Website', command=self.submit).grid(row=13,column=1,padx=5,pady=5, sticky='e')
        ttk.Button(self.frame_content,text='Clear All',command=self.clear).grid(row=13,column=2,padx=5,pady=5,sticky='w')
        ttk.Button(self.frame_content, text='Import Record',command=self.buttClick).grid(row=12,column=2,padx=5,pady=5,sticky='w')
        ttk.Button(self.frame_content, text='Add Record',command=self.addRecord).grid(row=12,column=3,padx=5,pady=5,sticky='w')

#-------------------------FUNCTIONS-------------------------#

        # SELECT each field

    def getSynopsis(self):
        varID = (self.contentBox.get())[0:2]
        print (varID)
        c.execute(("SELECT Synopsis FROM Movies WHERE ID ='{}'").format(varID))
        return c.fetchall()

    def getTitle(self):
        varID = (self.contentBox.get())[0:2]
        c.execute(("SELECT Title FROM Movies WHERE ID ='{}'").format(varID))
        return c.fetchall()

    def getCast(self):
        varID = (self.contentBox.get())[0:2]
        c.execute(("SELECT Actors FROM Movies WHERE ID ='{}'").format(varID))
        return c.fetchall()

    def getRating(self):
        varID = (self.contentBox.get())[0:2]
        c.execute(("SELECT Rating FROM Movies WHERE ID ='{}'").format(varID))
        return c.fetchall()

    def getDates(self):
        varID = (self.contentBox.get())[0:2]
        c.execute(("SELECT Dates FROM Movies WHERE ID ='{}'").format(varID))
        return c.fetchall()

    def getRuntime(self):
        varID = (self.contentBox.get())[0:2]
        c.execute(("SELECT Runtime FROM Movies WHERE ID ='{}'").format(varID))
        return c.fetchall()

    def getTrailer(self):
        varID = (self.contentBox.get())[0:2]
        c.execute(("SELECT Trailer FROM Movies WHERE ID ='{}'").format(varID))
        return c.fetchall()

    def getImage(self):
        varID = (self.contentBox.get())[0:2]
        c.execute(("SELECT Image FROM Movies WHERE ID ='{}'").format(varID))
        return c.fetchall()

    # Combo Box

    def getRecord(self):
        balls = self.contentBox.get()[0:2]
        print (balls)
        c.execute(("SELECT * FROM Movies WHERE ID ='{}'").format(balls))
        return c.fetchall()

##    def buttImport(self):
##        varID = self.getRecord()

    def forComboBox(self):
        c.execute("SELECT ID, Format, Title FROM Movies ORDER BY ID DESC LIMIT 0,9")
        return c.fetchall()






    def buttClick(self):

        self.clear()
 
        title = str(self.getTitle())[3:-4] # Insert field into textbox
        self.text_title.insert(1.0, title)

        dates = str(self.getDates())[3:-4] # Insert field into textbox
        self.text_date2d.insert(1.0, dates)

        synopsis = str(self.getSynopsis())[3:-4] # Insert field into textbox
        self.text_summary.insert(1.0, synopsis)

        cast = str(self.getCast())[3:-4] # Insert field into textbox
        self.text_cast.insert(1.0, cast)

        runtime = str(self.getRuntime())[3:-4] # Insert field into textbox
        self.text_runtime.insert(1.0, runtime)

        rating = str(self.getRating())[3:-4] # Insert field into textbox
        self.text_rating.insert(1.0, rating)

        trailer = str(self.getTrailer())[3:-4] # Insert field into textbox
        self.text_trailer.insert(1.0, trailer)

        image = str(self.getImage())[3:-4] # Insert field into textbox
        self.text_image.insert(1.0, image)

        # Maybe put this in a different function
        datesTemp = str(self.getDates()).split(',', 1)[0] # Grab the first day from date field
        datesEpoch = datesTemp[3:]+', ' + str(date.today().year) # Slice the ends off and add current year
        date_time = datesEpoch # Not sure what this is for
        pattern = '%B %d, %Y' # Tell python what the date format is
        epoch = int(time.mktime(time.strptime(date_time, pattern))) # Convert it to Epoch
        print (epoch)



    def addRecord(self):
        newTitle = self.text_title.get(1.0, 'end')
        newSynopsis = self.text_summary.get(1.0, 'end')
        newCast = self.text_cast.get(1.0, 'end')
        newRuntime = self.text_runtime.get(1.0, 'end')
        newRating = self.text_rating.get(1.0, 'end')
        newTrailer = self.text_trailer.get(1.0, 'end')
        newDates = self.text_date2d.get(1.0, 'end')
        newImage = self.text_image.get(1.0, 'end')
        
        c.execute('INSERT INTO Movies (Title, Synopsis, Actors, Runtime, Rating, Trailer, Dates, Image) VALUES ("{}","{}","{}","{}","{}","{}","{}","{}");'
                  .format(newTitle[:-1], newSynopsis[:-1], newCast[:-1], newRuntime[:-1], newRating[:-1], newTrailer[:-1], newDates[:-1], newImage[:-1]))
        conn.commit()
        self.addChunk1()

    def addChunk1(self):
        newChunk = self.chunk.format((self.text_title.get(1.0,'end')),
           (self.text_date2d.get(1.0,'end')),
           (self.text_date3d.get(1.0,'end')),
           (self.text_cast.get(1.0,'end')),
           (self.text_summary.get(1.0,'end')),
           (self.text_runtime.get(1.0,'end')),
           (self.text_trailer.get(1.0,'end')),
           (self.text_image.get(1.0,'end')),
           (self.text_rating.get(1.0,'end')))
        print (newChunk)
        return str(newChunk)

        # Creates and writes html file
    def createHTML(self, content):
        file = open("index.html", "w")
        file.write(content)
        file.close()
        
        # Takes content from textbox for use in createHTML() function
    def submit(self):
        self.createHTML(('''
<base href="http://www.SunsetTheatre.com/">
<html>

<head>



<!-- Facebook Pixel Code -->
<script>
!function(f,b,e,v,n,t,s){{if(f.fbq)return;n=f.fbq=function(){{n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)}};if(!f._fbq)f._fbq=n;
n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}}(window,
document,'script','//connect.facebook.net/en_US/fbevents.js');

fbq('init', '1528275494152372');
fbq('track', "PageView");</script>
<noscript><img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id=1528275494152372&ev=PageView&noscript=1"
/></noscript>
<!-- End Facebook Pixel Code -->



<link rel="shortcut icon" href="/favicon.ico" >

<meta name="description" content="movie theater - movie theatre & video store - Sunset Theatre - video rental - disc repair service - Summer Rocks Show - Connell Washington">

<meta http-equiv="Content-Type"
content="text/html; charset=iso-8859-1">
<meta name="GENERATOR" content="Sunset Theatre, all rights reserved.">
<title>Movie Theatre - Video Store - Sunset Theatre and Video</title>




<SCRIPT LANGUAGE='JAVASCRIPT' TYPE='TEXT/JAVASCRIPT'>
<!--
var popupWindow=null;
function popup(mypage,myname,w,h,pos,infocus){{

if (pos == 'random')
{{LeftPosition=(screen.width)?Math.floor(Math.random()*(screen.width-w)):100;TopPosition=(screen.height)?Math.floor(Math.random()*((screen.height-h)-75)):100;}}
else
{{LeftPosition=(screen.width)?(screen.width-w)/2:100;TopPosition=(screen.height)?(screen.height-h)/2:100;}}
settings='width='+ w + ',height='+ h + ',top=' + TopPosition + ',left=' + LeftPosition + ',scrollbars=no,location=no,directories=no,status=no,menubar=no,toolbar=no,resizable=no';popupWindow=window.open('',myname,settings);
if(infocus=='front'){{popupWindow.focus();popupWindow.location=mypage;}}
if(infocus=='back'){{popupWindow.blur();popupWindow.location=mypage;popupWindow.blur();}}

}}
// -->
</script>








<style>
.shakeimage{{
position:relative
}}
</style>
<script language="JavaScript1.2">

/*
Shake image script (onMouseover)- 
© Dynamic Drive (www.dynamicdrive.com)
For full source code, usage terms, and 100's more DHTML scripts, visit http://dynamicdrive.com
*/

//configure shake degree (where larger # equals greater shake)
var rector=1.5

///////DONE EDITING///////////
var stopit=0 
var a=1

function init(which){{
stopit=0
shake=which
shake.style.left=0
shake.style.top=0
}}

function rattleimage(){{
if ((!document.all&&!document.getElementById)||stopit==1)
return
if (a==1){{
shake.style.top=parseInt(shake.style.top)+rector
}}
else if (a==2){{
shake.style.left=parseInt(shake.style.left)+rector
}}
else if (a==3){{
shake.style.top=parseInt(shake.style.top)-rector
}}
else{{
shake.style.left=parseInt(shake.style.left)-rector
}}
if (a<4)
a++
else
a=1
setTimeout("rattleimage()",50)
}}

function stoprattle(which){{
stopit=1
which.style.left=0
which.style.top=0
}}

</script>















</head>


<style="font-family:verdana">

<body bgcolor="#" text="#FFFF00" link="yellow" alink="red" vlink="blue">







<font face="arial">

<center>





<br><br>




<img src="http://www.SunsetTheatre.com/images/fabuloussunset.jpg"><br><br>




<FONT color=yellow>
<center>

<font size=5>
<FONT color="red">Since 1952<br>
<h3><font color="yellow">
Franklin and Columbia, Connell WA<br>

</h3></b></center>


<font size=3>


<a href="http://www.SunsetTheatre.com/sunsetvideo.html" ALT="To the Video Store.">
<img src="http://www.SunsetTheatre.com/images/button2.gif" border="no" class="shakeimage" onMouseover="init(this);rattleimage()" onMouseout="stoprattle(this);top.focus()" onClick="top.focus()"></a>

<a href="http://www.SunsetTheatre.com/sunsethistory.html" ALT="Learn more about the Sunset...">
<img src="http://www.SunsetTheatre.com/images/button3.gif" border="no" class="shakeimage" onMouseover="init(this);rattleimage()" onMouseout="stoprattle(this);top.focus()" onClick="top.focus()"></a>

<a href="http://www.SunsetTheatre.com/DVD.html" ALT="DVDs available at the Video Store.">
<img src="http://www.SunsetTheatre.com/images/button4.gif" border="no" class="shakeimage" onMouseover="init(this);rattleimage()" onMouseout="stoprattle(this);top.focus()" onClick="top.focus()"></a>

<a href="http://www.SunsetTheatre.com/srs.html" ALT="To the Summer Rocks Show!">
<img src="http://www.SunsetTheatre.com/images/button6.gif" border="no" class="shakeimage" onMouseover="init(this);rattleimage()" onMouseout="stoprattle(this);top.focus()" onClick="top.focus()"></a>

<a href="http://www.SunsetTheatre.com/Information.html" ALT="Be informed.">
<img src="http://www.SunsetTheatre.com/images/button7.gif" border="no" class="shakeimage" onMouseover="init(this);rattleimage()" onMouseout="stoprattle(this);top.focus()" onClick="top.focus()"></a>



<br><br>


The Sunset Theatre is a classic 1950s single screen small town movie theatre.<br>Built in 1952, it was originally called the Aubert Theatre.  It became The Sunset after a truck damaged the marquee.<br>For more information check out the <a href="http://www.SunsetTheatre.com/sunsethistory.html">history page</a>, or scroll down to see what's playing.<br><br>


<FONT color="red"><b>Showtime:<br>
<font color="yellow">7:30pm</b><br>
Friday, Saturday & Sunday unless otherwise noted.<br><br>


<FONT color="red"><b>Admission Prices:</b><br>

<font color="yellow">Adults: <b>$7.00, <font color="DodgerBlue">3D: $8.00</b><br>
<font color="yellow">Students (12-16): <b>$6.00, <font color="DodgerBlue">3D: $7.00</b><br>
<font color="yellow">Children (3-11) & Seniors (65 & over): <b>$5.00, <font color="DodgerBlue">3D: $6.00</b><br><font color="yellow">
<br>
<IMG src="http://www.sunsettheatre.com/images/credit.gif"><br>

We gladly accept Visa and Mastercard.<br><br>



<p><a href="http://www.SunsetTheatre.com/sunsetvideo.html" target="_blank">
<img src="http://www.SunsetTheatre.com/images/beforeandafterdvdsmall.jpg" border="no"><br>
<font color="#00FF00" size="3"><strong>Learn about our Disc Repair Service on the Video Store Page.</a></strong></font></p>


<p><a href="http://www.SunsetTheatre.com/employmentapplication.pdf" target="_blank">
<img src="http://www.SunsetTheatre.com/images/employment.jpg" border="no"><br>
<font color="#00FF00" size="3"><strong>For a Sunset Theatre Employment Application click here.</a></strong></font></p>

<hr>


{0}







<iframe src="https://www.dealflicks.com/banners/468x60" frameborder=0 width=468 height=60></iframe>
<br><br>


<font color="#00FF00" size="3"><b>

For information about our 2012 Digital Conversion  
<a href="http://www.SunsetTheatre.com/Information.html" target="_blank">click here.</a>
<br>
For more information about movie ratings  
<a href="http://www.filmratings.com" target="_blank">click here.</a>
<br>
For the current top movies  
<a href="http://www.boxofficemojo.com/weekend/chart/" target="_blank">click here.</a>
<br>
To see what the critics think  
<a href="http://www.metacritic.com/" target="_blank">click here.</a>
</b></font>

<hr>

<FONT color="red" size="5"><b>Past Movies:</b><br>
<FONT color=yellow size="3">



<br><br>

<a href="http://www.SunsetTheatre.com/pastmovies.html"><img src=http://www.SunsetTheatre.com/images/schedulessmall.jpg border="no"><br>
<b>For a complete list of all the movies we've played click here.</b></a>

<hr>


<img src="http://www.SunsetTheatre.com/images/artifacts4s.jpg"><br><hr>


<center>
<img src=http://www.SunsetTheatre.com/images/anniversarysticker2.jpg><br>
<font color=yellow><br>
<font size=3>
The Aubert Theatre as it was originally called, opened September 4th, 1952.<br>
2002 marked its 50th year as well as the 10th year of its current ownership.<br>
Thank you for supporting your local movie theatre!<br><br>


<FONT color=yellow>

<A href="http://www.sunsettheatre.com/sunsethistory.html" ALT="History of the Theatre">
<FONT color=yellow>See some historical pictures here!</A><br><br> 
<hr>




</STRONG></FONT></P>


<img src=http://www.SunsetTheatre.com/images/Deb1a.jpg>
<img src=http://www.SunsetTheatre.com/images/Deb2.jpg><br>
<FONT color=#8080ff>
Two of our patrons necking in the back row...
<hr>
<FONT color=red><i>"It's kind of a warm fuzzy feeling knowing you've got a theatre in town."</i><br>-Dave Gribble<br><hr></h5>





<center><FONT color=#8080ff>
<img src="http://www.SunsetTheatre.com/images/robber.jpg"><br>
One of our patrons enjoying the show. 
<hr><br>

<font color=red><font size=5><img src="http://www.SunsetTheatre.com/images/franklincolumbia.jpg"><br>
<b>The Sunset Theatre is located in the Center of Town<br>
which, it turns out, is also the exact center of the universe.</b><br><br>

<a href="http://maps.google.com/maps?ie=UTF8&oe=utf-8&client=firefox-a&q=sunset+theatre&near=Connell,+WA&fb=1&cid=0,0,5800163222293295548&ll=46.661307,-118.861309&spn=0.003129,0.007231&z=17&iwloc=A&om=1" target="_blank">
<img src=http://www.SunsetTheatre.com/images/mappymap.jpg><br>
<font size=3>
Click here for a detailed map.</a><br>


<hr>

<center>
<img src="http://www.SunsetTheatre.com/images/marqueee.gif">

<p align="center"><font color="red" size="6"><strong>Thank
you for visiting the Sunset Theatre Website!</p>

<SCRIPT LANGUAGE="JavaScript">
<!-- Begin
todaydate = new Date();
timeis=todaydate.getTime();
todaydate.setTime(timeis);
houris = todaydate.getHours();
if (houris > 16) display = "Evening";
else if (houris >11) display = "Afternoon";
else display = "Morning";
var welcome = ("Have a Good " + display + "!");
document.write(welcome);
// End -->
</script>



<p align="center"><IMG src="http://www.sunsettheatre.com/images/phone.gif">
<font color="#8080FF" size="6"><center>
<strong>(509) 234-7811</strong></font>

<p align="center"><IMG src="http://www.sunsettheatre.com/images/emailbox.gif">
<FONT color=red>
<font size=2><center>


<A HREF="mailto:&#100;&#105;&#114;&#107;&#64;&#115;&#117;&#110;s&#101;&#116;t&#104;e&#97;tre.&#99;&#111;&#109;">
&#100;&#105;&#114;&#107;&#64;&#115;&#117;&#110;s&#101;&#116;t&#104;e&#97;tre.&#99;&#111;&#109;</A>
Sunset Theatre and Video, 102 N Columbia, PO Box 827, Connell WA 99326
<br>
<br>




<hr>

<font size=3>


<center>


<br>

<IMG src="http://www.sunsettheatre.com/images/cool6.gif">

<br><br>




<p><a href="http://www.youtube.com/watch?v=Pi8eGFAwGdg" target="_blank">
<img src="http://www.SunsetTheatre.com/images/fandomicity.jpg" border=no><br>
Watch Nathan's Pam Pong video here.</a></b></p>

<p><font color="#00FF00" size="3"><strong>
<a href="http://www.cinematour.com" target="_blank">
<img src="http://www.SunsetTheatre.com/images/cinematour.jpg" border="no"><br>
Cinematour is a very cool website about 
movie theatres around the world.</a></strong></font></p>

<p><font color="#00FF00" size="3"><strong>
<a href="http://cinematreasures.org/" target="_blank"><img src="http://www.SunsetTheatre.com/images/cinematreasures.jpg" border="no"><br>
Here is another one: Cinema Treasures.</a></strong></font></p>

<p><font color="#00FF00" size="3"><strong>
<a href="http://www2.hawaii.edu/~angell/thsa/welcome2.html" target="_blank"><img src="http://www.SunsetTheatre.com/images/chinese.bmp" border="no"><br>And another: The Theatre Historical Society of America.</a></strong></font></p>

<p><a href="http://manleypopcornmachine.com" target="_blank">
<img src="http://www.SunsetTheatre.com/images/manleyresize.jpg" border=no><br>
Here is a great website all about old Manley Popcorn Machines like ours.</a></b></p>


<p><font color="#00FF00" size="3"><strong>
</strong></font></p>



<p><a href="http://www.cityofconnell.com" target="_blank">
<img src="http://www.SunsetTheatre.com/images/connelllogo.jpg" border="no"><br>
<font color="#00FF00" size="3">
<strong>Learn more about the City of Connell here.</a></strong></font></p>
<p><font color="#00FF00" size="3">
<strong>...and <a href="http://www.city-data.com/city/Connell-Washington.html" target="_blank">here.</a></strong></font></p>

<p><a href="http://www.wheresgeorge.com" target="_blank">
<img src="http://www.SunsetTheatre.com/images/george_eyes.gif" border="no"><br>
<font color="#00FF00" size="3">
<strong>Where's George?</a></strong></font></p>

<a href="http://www.myspace.com/comebacks" target="_blank"><img src="http://www.sunsettheatre.com/images/disss.jpg" border="no"><br>Sweet Diss and the Comebacks</a>
<br><br>

<FONT color=yellow>



<hr>
<!-- Start Bravenet.com Service Code -->
<div align="center">
<div style="width:128; padding:2px; border:2px solid #ffee00; background-color:#; color:#FFEE22; font:normal normal bold 18px times; text-decoration:none">
Visitors:
<!-- DO NOT MODIFY -->
<script language="JavaScript" type="text/javascript" src="http://pub12.bravenet.com/counter/code.php?id=340224&usernum=973092419&cpv=2&bc=FFEE00&bw=1"></script>
<!-- END DO NOT MODIFY -->
</div></div>
<!-- End Bravenet.com Service Code -->

<br><b>

<a href="http://www.twitter.com/sunsettheatre" target="_blank"><img src="http://twitter-badges.s3.amazonaws.com/follow_me-a.png" border="no" alt="Follow sunsettheatre on Twitter"/></a>

<br>


<script type="text/javascript" src="http://static.ak.connect.facebook.com/js/api_lib/v0.4/FeatureLoader.js.php/en_US"></script><script type="text/javascript">FB.init("cda89cbf5367c5fcbe0597c312229638");</script><fb:fan profile_id="5915832161" stream="" connections="10" width="300"></fb:fan><div style="font-size:8px; padding-left:10px"><a href="http://www.facebook.com/pages/Connell-WA/Sunset-Theatre-Video/5915832161">Sunset Theatre & Video on Facebook</a> </div>

<br>

<a href="javascript:window.print()">Print This Page</a><br><br>
<a href="javascript:window.external.AddFavorite('http://www.sunsettheatre.com/', 'Sunset Theatre & Video');">
Bookmark This Site</a><br>
<br>


<font color="#00FF00" size="3">
<strong>To the <a href="http://www.1966batmobile.com/" target="_blank">Batmobile!</a></strong></font></p>

<img src=http://www.SunsetTheatre.com/images/sunsetcccold2.jpg><br><br>
</b>
<font color="white"><a href="http://www.natoonline.org" target="_blank"">
<img src=http://www.SunsetTheatre.com/images/natologo.jpg  border="no"><br>Member, National Association of Theatre Owners</a><br><br>
</font>
All information is subject to change without notice.<br>
<br>

<a href="http://www.SunsetTheatre.com/sunsetvideo.html" ALT="To the Video Store.">
<img src="http://www.SunsetTheatre.com/images/button2.gif" border="no" class="shakeimage" onMouseover="init(this);rattleimage()" onMouseout="stoprattle(this);top.focus()" onClick="top.focus()"></a>

<a href="http://www.SunsetTheatre.com/sunsethistory.html" ALT="Learn more about the Sunset...">
<img src="http://www.SunsetTheatre.com/images/button3.gif" border="no" class="shakeimage" onMouseover="init(this);rattleimage()" onMouseout="stoprattle(this);top.focus()" onClick="top.focus()"></a>

<a href="http://www.SunsetTheatre.com/DVD.html" ALT="DVDs available at the Video Store.">
<img src="http://www.SunsetTheatre.com/images/button4.gif" border="no" class="shakeimage" onMouseover="init(this);rattleimage()" onMouseout="stoprattle(this);top.focus()" onClick="top.focus()"></a>

<a href="http://www.SunsetTheatre.com/srs.html" ALT="To the Summer Rocks Show!">
<img src="http://www.SunsetTheatre.com/images/button6.gif" border="no" class="shakeimage" onMouseover="init(this);rattleimage()" onMouseout="stoprattle(this);top.focus()" onClick="top.focus()"></a>

<a href="http://www.SunsetTheatre.com/Information.html" ALT="Be informed.">
<img src="http://www.SunsetTheatre.com/images/button7.gif" border="no" class="shakeimage" onMouseover="init(this);rattleimage()" onMouseout="stoprattle(this);top.focus()" onClick="top.focus()"></a>

<br><br><i>"Support Your Local Movie Theatre."</i><br>

</b>
</font>
</body>
</html>
'''.format(self.addChunk1())))
##           (self.pastMovies()))))

        # Confirmation of submission via dialog box
        messagebox.showinfo(title='Web page created successfully!',message=
                            "Success! Now just upload this index.html file to the server.")

        # Clears textbox on Clear click
    def clear(self):
        self.text_title.delete(1.0,'end')
        self.text_cast.delete(1.0,'end')
        self.text_date2d.delete(1.0,'end')
        self.text_date3d.delete(1.0,'end')
        self.text_summary.delete(1.0,'end')
        self.text_trailer.delete(1.0,'end')
        self.text_runtime.delete(1.0,'end')
        self.text_image.delete(1.0,'end')
        self.text_rating.delete(1.0,'end')

    chunk = ('''
<img src=http://www.SunsetTheatre.com/images/Reel2.gif><br>
<b><font color="yellow" size="5">
{1}<br>
{2}<br>

<br>

<img src="http://www.SunsetTheatre.com/images/{7}">
<font color="red" size="7">
<br>{0}<br>

<img src="http://www.SunsetTheatre.com/images/dlp.png">
<img src="http://www.SunsetTheatre.com/images/spacer.jpg"><img src="http://www.SunsetTheatre.com/images/dolby7.1.jpg">

<FONT color=yellow size=3>
</b><br><b>

{3}

</b><br><br>

{4}<br><br> 

<img src="http://www.SunsetTheatre.com/images/PG.jpg"><br>
Running Time: {5}
<br><br>

<a href="https://www.youtube.com/watch?v={6}" target="_blank"><img src="http://www.SunsetTheatre.com/images/watchtrailer.jpg" border="no"></a>
<img src="http://www.SunsetTheatre.com/images/spacer.jpg">
<a href="https://www.dealflicks.com/theaters/sunset-theatre-and-video" target="_blank"><img src="http://www.SunsetTheatre.com/images/buyticketssmall.gif" border="no"></a><br>
<hr>
''')
        
# Run program          
def main():            
    
    root = Tk()
    guihtml = GUIhtml(root)
    root.mainloop()
    
if __name__ == "__main__": main()
