document.addEventListener("DOMContentLoaded", function () {
  const startButton = document.getElementById("start-button");
  const stopButton = document.getElementById("stop-button");
  const responseDiv = document.getElementById("response");

  // Establish WebSocket connection
  const socket = new WebSocket("ws://localhost:8000/ws");

  // Handle WebSocket messages
  socket.onmessage = function (event) {
    responseDiv.innerText = event.data;
    if (
      event.data.includes("Script has finished running") ||
      event.data.includes("Script stopped by user")
    ) {
      stopButton.classList.remove("highlight");
    }
  };

  // Handle button click to start the script
  startButton.addEventListener("click", function () {
    const endTime = document.getElementById("end-time").value;
    fetch("/start", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ end_time: endTime }),
    })
      .then((response) => response.json())
      .then((data) => {
        responseDiv.innerText = data.status;
        stopButton.classList.add("highlight");
      });
  });

  // Handle button click to stop the script
  stopButton.addEventListener("click", function () {
    fetch("/stop", {
      method: "POST",
    })
      .then((response) => response.json())
      .then((data) => {
        responseDiv.innerText = data.status;
        stopButton.classList.remove("highlight");
      });
  });
});
