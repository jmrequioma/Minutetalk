// replace these values with those generated in your TokBox Account
var apiKey = "46145962";
var sessionId = "1_MX40NjE0NTk2Mn5-MTUzMDI1NTgzMDY1Nn5qVGEzNTRZdzZ2TnpIK05NODJMamgwOGN-UH4";
var token = "T1==cGFydG5lcl9pZD00NjE0NTk2MiZzaWc9ODVmN2ZmMGFjNTA2MWIyYjZmMDg0Nzg5OTUwZDZjYjhlZDI5Mzc2MDpzZXNzaW9uX2lkPTFfTVg0ME5qRTBOVGsyTW41LU1UVXpNREkxTlRnek1EWTFObjVxVkdFek5UUlpkeloyVG5wSUswNU5PREpNYW1nd09HTi1VSDQmY3JlYXRlX3RpbWU9MTUzMDI1NTg5MSZub25jZT0wLjAyNjIzNjEyOTIxNDQ3OTA0MyZyb2xlPXB1Ymxpc2hlciZleHBpcmVfdGltZT0xNTMyODQ3ODg5JmluaXRpYWxfbGF5b3V0X2NsYXNzX2xpc3Q9";

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