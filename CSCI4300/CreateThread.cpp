//Holden Davis - Lab 2
//10/14/22 - Fall 2022
//Dr. Sun - CSCI 4300 - CRN 22807

//Preprocessor directive to use basic console input/output commands
#include <stdio.h>
//Preprocessor directive to use Win32 API
#include <windows.h>
//Preprocessor directive to use advanced math functions (power command, in this instance)
#include <cmath>

//Global variable to store result of thread computation
DWORD Result;

//Thread function - computes and returns the result of Param (the input number) to the power of itself; eg. 2 ^ 2 = 4, 3 ^ 3 = 27
DWORD WINAPI Power(LPVOID Param)
{
    //Cast input parameter of type LPVOID to DWORD to use in numerical computation
    DWORD Number = *(DWORD*)Param;
    //Compute the power and store in global DWORD variable for later access in main()
    Result = pow(Number, Number);
    //Return zero to calling function
    return 0;
}

//Entry point!
int main(int argc, char *argv[])
{
    //Define DWORD to store the ID of the created thread and HANDLE to store the handle of the created thread
    DWORD ThreadId;
    HANDLE ThreadHandle;
    //Integer to store command line input variable once converted to integer from string
    int Param;
    //If argc < 2 (we didn't include the number argument), alert user of the error and return -1 to main
    if (argc != 2){
        fprintf(stderr, "A valid integer is required for computation!\n");
        return -1;
    }
    //Cast argument to a integer 
    Param = atoi(argv[1]);
    //If the argument is a negative number (we only want to compute the power of positive numbers here), alert user of the error and return -1 to main 
    if (Param < 0) {
        fprintf(stderr, "Integer must be non-negative to compute the power!\n");
        return -1;
    }
    //Create the thread and store the result in Threadhandle
    ThreadHandle = CreateThread(
        NULL,           //Leave security attributes null
        0,              //Leave stack size at zero
        Power,          //Set start routine to our power function; this is what the thread actually executes
        &Param,         //Pass in address of our converted integer parameter
        0,              //Standard creation flags
        &ThreadId       //Pass in the address of our ThreadId variable 
    );
    //If threadhandle is not null, the thread was successfully created
    if (ThreadHandle != NULL)
    {
        //Wait for the thread (referenced by its handle) for an infinite amount of time
        WaitForSingleObject(ThreadHandle, INFINITE);
        //Once the thread is finished, close it by again referencing its handle
        CloseHandle(ThreadHandle);
        //The thread's computation is finished and stored in the Result global variable, so we can output that!
        printf("Result = %d\n", Result);
    }
    //Return 0 to main, we're all done!
    return 0;
}