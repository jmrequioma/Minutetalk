// replace these values with those generated in your TokBox Account
var apiKey = "46151822";
var sessionId = "1_MX40NjE1MTgyMn5-MTUzMTM4MzcwMDk2NX4wQ29icndnTEhhMWo5Z0x1T1NQMUZkb1d-UH4";
var token = "T1==cGFydG5lcl9pZD00NjE1MTgyMiZzaWc9YTZjODgxMmM3NWVjMThlMDkyN2VmN2E1MThmMTJjZmE5NjYxM2EwNDpzZXNzaW9uX2lkPTFfTVg0ME5qRTFNVGd5TW41LU1UVXpNVE00TXpjd01EazJOWDR3UTI5aWNuZG5URWhoTVdvNVoweDFUMU5RTVVaa2IxZC1VSDQmaW5pdGlhbF9sYXlvdXRfY2xhc3NfbGlzdD0mbm9uY2U9NDAyJmNyZWF0ZV90aW1lPTE1MzEzODYzMTAmZXhwaXJlX3RpbWU9MTUzMTQ3MjcxMCZyb2xlPXB1Ymxpc2hlcg==";

// Handling all of our errors here by alerting them
function handleError(error) {
  if (error) {
    alert(error.message);
  }
}

function initializeSession() {
  var session = OT.initSession(apiKey, sessionId);

  // Subscribe to a newly created stream
  session.on('streamCreated', function(event) {
  session.subscribe(event.stream, 'subscriber', {
    insertMode: 'append',
    width: '100%',
    height: '100%'
  }, handleError);
});

  // Create a publisher
  var publisher = OT.initPublisher('publisher', {
    insertMode: 'append',
    width: '100%',
    height: '100%'
  }, handleError);

  // Connect to the session
  session.connect(token, function(error) {
    // If the connection is successful, publish to the session
    if (error) {
      handleError(error);
    } else {
      session.publish(publisher, handleError);
    }
  });
}
// (optional) add server code here
initializeSession();