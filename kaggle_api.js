/*
    USE THIS CODE WITH CAUTION
    ITS AN AI-GENERATED CODE
    Good Luck!
*/ 

const { spawn } = require('child_process');

const command = 'kaggle -h'; // Replace with your desired command

const process = spawn('cmd.exe', ['/c', command]);

process.stdout.on('data', (data) => {
    console.log(data.toString());
});

process.stderr.on('data', (data) => {
    console.error(data.toString());
});

process.on('close', (code) => {
    console.log(`Process exited with code: ${code}`);
});
