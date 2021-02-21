# Security-Camera
DESCRIPTION:

I've decided to make a motion detecting secuirty camera for my home by utlizing Python and Rasberry pi (In Progress Project)
This project uses Python's CV library to detect motion detetction from a still frame. Upon its detection it creates a border frame by indetifying the object. It records the time stamp from when the object enters and leaves the frame which then exports the data to a csv file. Using Python's Bokeh library (similar to matplotlib) the data in the csv file is visualized into a graph to show the increase in motion detection.

Use of Raspberry Pi 4 and Picamera:

In order to make a functioning camera, the project uses Raspberry Pi 4 and the Picamera extension for it to work. The Python script is used in conjunction with Raspberry Pi upon booting it up.

Future Plans:

-Able to send alert emails to your gmail account when motion is detected.

-A video clip is attached next to the time stamp graph in order to view the motion at x time.




Below are some screenshots to show a high level overview of it:

<img width="893" alt="Screen Shot 2021-02-20 at 8 04 01 PM" src="https://user-images.githubusercontent.com/40875745/108616685-8bbaee00-73c4-11eb-9c52-964d66016389.png">


<img width="863" alt="Screen Shot 2021-02-20 at 8 03 43 PM" src="https://user-images.githubusercontent.com/40875745/108616699-b9a03280-73c4-11eb-88c8-eda5baf6601f.png">


<img width="1382" alt="Screen Shot 2021-02-20 at 7 55 22 PM" src="https://user-images.githubusercontent.com/40875745/108616701-bc028c80-73c4-11eb-8439-a20c1e632e32.png">
