const startRecordingBtn = document.getElementById("recordButton");
const stopRecordingBtn = document.getElementById("stopButton");
const pauseButton = document.getElementById("pauseButton");
var form1=document.getElementById("form1");
var form2=document.getElementById("form2");
var waveform1=document.getElementById("waveform1");
//add events to those 2 buttons
let audioCtx;
let recorder;
let stream;

navigator.mediaDevices
  .getUserMedia({ audio: true, video: false })
  .then((_stream) => {
    stream = _stream;
    audioCtx = new AudioContext();
    const microphone = audioCtx.createMediaStreamSource(stream);
    // Create a new recorder
    recorder = new Recorder(microphone, {sampleRate: 11025,numChannels: 1});
    startRecordingBtn.addEventListener("click", startRecording);
    stopRecordingBtn.addEventListener("click", stopRecording);
    pauseButton.addEventListener("click", pauseRecording);
    wavesurfer()
  })
  .catch((error) => {
    console.error("Error getting audio stream:", error);
  });
  let wavesurfer1;

  function wavesurfer(){
    wavesurfer1 = WaveSurfer.create({
      container: "#waveform1",
      waveColor: "violet",
      progressColor: "purple",
      height: 128,
      barWidth: 3,
      cursorWidth: 1,
      cursorColor: "#333",
      responsive: true
    });}
  function startRecording() {
    // Start recording
   
    stopRecordingBtn.removeAttribute("disabled");
    startRecordingBtn.setAttribute("disabled", true);
    pauseButton.removeAttribute("disabled");
    recorder.record();
  }

function pauseRecording(){
    console.log("pauseButton clicked rec.recording=",rec.recording );
    if (recorder.recording){
        //pause
        recorder.stop();
        pauseButton.innerHTML="Resume";
    }else{
        //resume
        recorder.record()
        pauseButton.innerHTML="Pause";

    }
}
  
function stopRecording() {
  
  stopRecordingBtn.setAttribute("disabled", true);
  
  pauseButton.setAttribute("disabled", true);
  recorder.stop();
  form1.style.display="inline";
  form2.style.display="block";
  
  recorder.exportWAV(blob => {
    var url = URL.createObjectURL(blob);
    var au = document.createElement('audio');
    var li = document.createElement('li');
    var link = document.createElement('a');
    create(url,au,li,link);
  });
}

function create(url,au,li,link) {

    

    //name of .wav file to use during upload and download (without extendion)
    var filename = new Date().toISOString();

    //add controls to the <audio> element
    au.controls = true;
    au.src = url;
    waveform1.style.display="block";
    wavesurfer1.load(url);
    au.addEventListener("play",function(){wavesurfer1.playPause();});
    au.addEventListener("pause",function(){wavesurfer1.pause();});
    //save to disk link
    link.href = url;
    link.download = filename+".wav"; //download forces the browser to download the file using the  filename
    link.innerHTML = "Save to disk";

    //add the new audio element to li
    li.appendChild(au);

    //add the filename to the li
    li.appendChild(document.createTextNode(filename+".wav "))

    //add the save to disk link to li
    li.appendChild(link);
    
// Create a new Blob
//
let myBlob = null;

// Fetch the audio file at the URL
fetch(url)
  .then(response => response.blob())
  .then(blob => {
    myBlob = blob;
  });
    //upload link
    var upload = document.createElement('a');
    upload.href="#";
    upload.innerHTML = "Upload";
    upload.addEventListener("click", function(event){
          var xhr=new XMLHttpRequest();
         
          xhr.onload=function(e) {
              if(this.readyState === 4) {
                  console.log("Server returned: ",e.target.responseText);
              }
          };
          var fd=new FormData();
          fd.append("audio_data",myBlob,`${filename}.wav`,{ type: 'audio/wav' });
          xhr.open("POST","/",true);
         
          xhr.send(fd);
    })
    li.appendChild(document.createTextNode (" "))//add a space in between
    li.appendChild(upload)//add the upload link to li

    //add the li element to the ol
    recordingsList.appendChild(li);
}
