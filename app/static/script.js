document.addEventListener("DOMContentLoaded", () => {
  const startForm = document.getElementById("start-form");
  const stopButton = document.getElementById("stop-button");
  const responseDiv = document.getElementById("response");

  startForm.addEventListener("submit", async (event) => {
    event.preventDefault();
    const endTime = document.getElementById("end-time").value;

    const response = await fetch("/start", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ end_time: endTime }),
    });

    const result = await response.json();
    responseDiv.textContent = result.status;
  });

  stopButton.addEventListener("click", async () => {
    const response = await fetch("/stop", {
      method: "POST",
    });

    const result = await response.json();
    responseDiv.textContent = result.status;
  });
});
