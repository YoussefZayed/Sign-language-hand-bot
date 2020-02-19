# Sign-language-hand-bot

Inspiration

We wanted to promote an easy learning system to introduce verbal individuals to the basics of American Sign Language. Often people in the non-verbal community are restricted by the lack of understanding outside of the community. Our team wants to break down these barriers and create a fun, interactive, and visual environment for users. In addition, our team wanted to replicate a 3D model of how to position the hand as videos often do not convey sufficient information.
What it does

Step 1 Create a Machine Learning Model To Interpret the Hand Gestures This step provides the foundation for the project. Using OpenCV, our team was able to create datasets for each of the ASL alphabet hand positions. Based on the model trained using Tensorflow and Google Cloud Storage, a video datastream is started, interpreted and the letter is identified.

Step 2 3D Model of the Hand The Arduino UNO starts a series of servo motors to activate the 3D hand model. The user can input the desired letter and the 3D printed robotic hand can then interpret this (using the model from step 1) to display the desired hand position. Data is transferred through the SPI Bus and is powered by a 9V battery for ease of transportation.
How I built it

Languages: Python, C++ Platforms: TensorFlow, Fusion 360, OpenCV, UiPath Hardware: 4 servo motors, Arduino UNO Parts: 3D-printed
Challenges I ran into

    Raspberry Pi Camera would overheat and not connect leading us to remove the Telus IoT connectivity from our final project

    Issues with incompatibilities with Mac and OpenCV and UiPath

    Issues with lighting and lack of variety in training data leading to less accurate results.

Accomplishments that I'm proud of

    Able to design and integrate the hardware with software and apply it to a mechanical application.
    Create data, train and deploy a working machine learning model

What I learned

How to integrate simple low resource hardware systems with complex Machine Learning Algorithms.
What's next for ASL Hand Bot

    expand beyond letters into words
    create a more dynamic user interface
    expand the dataset and models to incorporate more

