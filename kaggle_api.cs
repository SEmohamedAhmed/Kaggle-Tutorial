/*
    USE THIS CODE WITH CAUTION
    ITS AN AI-GENERATED CODE
    Good Luck!
*/ 

using System;
using System.Net.Http;
using System.Threading.Tasks;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using System.Diagnostics;

public class Program
{
    public static string Excute_Terminal_Command(string Command)
    {
        Process process = new Process();
        process.StartInfo.FileName = "cmd.exe";

        // Set UseShellExecute to false to avoid launching a shell window
        process.StartInfo.UseShellExecute = false;

        // Redirect standard output for capturing the command output (optional)
        process.StartInfo.RedirectStandardOutput = true;

        // Set the actual command you want to run as the argument
        process.StartInfo.Arguments = $"/c {Command}";

        process.Start();

        // Capture the output if needed
        if (process.StartInfo.RedirectStandardOutput)
        {
            process.WaitForExit();
            return process.StandardOutput.ReadToEnd();
        }

        process.WaitForExit();
        return "No Output Was Returned";
    }
    public static void Main(string[] args)
    {
        string Command = "kaggle kernels status mrmody476/isthisgppretrained-gp-vton";
        Console.WriteLine(Excute_Terminal_Command(Command));

        Command = "kaggle -h";
        Console.WriteLine(Excute_Terminal_Command(Command));
        Console.WriteLine("\n\n\n\n");
        var python_file_path = "mody2024.py"
        Command = $"python {python_file_path}";
        Console.WriteLine(Excute_Terminal_Command(Command));
    }
}
