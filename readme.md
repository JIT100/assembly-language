# **Assembly-like Program Execution**
___

This is a simple Python program that executes an assembly-like program containing `MV` (move constant into register), `ADD` (addition), and `SHOW` (display register value) instructions.

## **Requirements**
___

- Python 3.9 +
- Docker
- Docker Compose File

## **Instructions**
___

- Clone the repository to your local machine.
- Install Docker on the local Machine.
- Start the application with **`docker-compose up --build`** on terminal. ( Remove the build keyword to just start the application without having to build docker image.)

## **Usage**
___
*In this example program, the following actions are performed*:

- Move the value 2000 into REG1.
- Move the value 4000 into REG2.
- Add the values of REG1 and REG2, saving the result in REG1.
- Add 600 to the value in REG1, saving the result in REG1.
- Display the value in REG1.

### View the Results: 
The program will execute the instructions and display the result of the SHOW statement at the end. Additionally, the final values of all registers will be printed.

Example Output:
```
MV REG1 2000
MV REG2 4000
ADD REG1 REG2
ADD REG1 600
SHOW REG1 6600
```
### Editing the Assembler input:

Feel free to modify the provided example program or create your own program using the supported instructions. You can modify exiting Assembly instruction from `assembler.txt` file. 

Eg: Change the value of reg1 , from 2000 to 6000

You have to use **`docker-compose up --build`** to rebuild the image if you do edit the assember file.