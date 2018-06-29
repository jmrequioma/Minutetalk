// replace these values with those generated in your TokBox Account
var apiKey = "46145962";
var sessionId = "2_MX40NjE0NTk2Mn5-MTUzMDI0NTM3MzQzM35laXg1M3F0K0t0MDlrNE5aV2FoY3ZLck5-fg";
var token = "T1==cGFydG5lcl9pZD00NjE0NTk2MiZzaWc9ZTRhYmM4YmY4ZTNlZGNmNDRlZGUyMmQwNjBiMGZlZjFmYzk0NzM5NDpzZXNzaW9uX2lkPTJfTVg0ME5qRTBOVGsyTW41LU1UVXpNREkwTlRNM016UXpNMzVsYVhnMU0zRjBLMHQwTURsck5FNWFWMkZvWTNaTGNrNS1mZyZjcmVhdGVfdGltZT0xNTMwMjQ1NDMwJm5vbmNlPTAuMTg0MTQ3NDcxNDQwMjE3OCZyb2xlPXB1Ymxpc2hlciZleHBpcmVfdGltZT0xNTMwODUwMjMwJmluaXRpYWxfbGF5b3V0X2NsYXNzX2xpc3Q9";

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