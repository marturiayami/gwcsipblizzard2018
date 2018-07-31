function toUWU() {
  var englishInput = document.getElementById('word').value;
  var uwuOut = '';
    for (var i = 0; i < englishInput.length; i++){
      if ((englishInput.charAt(i) == 'r') || (englishInput.charAt(i) == 'l')){
        uwuOut +=  'w';
      }
      else if ((englishInput.charAt(i) == 'n') {
        uwuOut += 'ny';
      }
      else if ((englishInput.charAt(i) == '!') {
        uwuOut += '~ uwu';
      }
      else {
        uwuOut += englishInput.charAt(i);
      }
    }
    document.getElementById('demo').innerHTML = uwuOut;
    console.log(uwuOut);
}
