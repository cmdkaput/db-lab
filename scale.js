const url = "https://cloudlab2containerapp.gentleforest-55b9a57f.norwayeast.azurecontainerapps.io/brand"; 


const data = {
  name: "LoadTest Equipment",
  description: "Created by load test",
  status: "Available",
  equipment_item_id: 1
};

async function sendRequest(i) {
  const res = await fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data)
  });
  console.log(`Request ${i + 1}: ${res.status}`);
}

(async () => {
  const tasks = [];
  for (let i = 0; i < 500; i++) {
    tasks.push(sendRequest(i));
  }
  await Promise.all(tasks);
})();