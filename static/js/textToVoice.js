// var msg = new SpeechSynthesisUtterance();
// var voices = window.speechSynthesis.getVoices();
// msg.volume = 1; // From 0 to 1
// msg.rate = 1; // From 0.1 to 10
// msg.pitch = 2; // From 0 to 2
// msg.text = 
// msg.lang = 'es';
// speechSynthesis.speak(msg);



const speak = (m) => {
    var speech = new SpeechSynthesisUtterance();

    speech.lang = "hi-IN";
    speech.text = m;
    speech.volume = 1;
    speech.rate = 1;
    speech.pitch = 1;
    // speech.voice = SpeechSynthesis.getVoice()[10]

    
    window.speechSynthesis.speak(speech);

}