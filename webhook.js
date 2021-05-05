const { Client, Intents } = require('discord.js');
const Discord = require('discord.js');
const fetch = require('node-fetch');
const fs = require('fs');
uptime = fs.readFileSync('uptime.txt').split(', ')

fetch('https://discord.com/api/webhooks/839274541850165278/wngPMrGfCWRn1jQhBDtai9fyFF7RP5flaIsetYhu8uhZbLwPglwre-2DokamuE_Smhhq').then(res => {
  return res.json();
}).then(function (json) {
  const webhook = new Discord.WebhookClient(json.id, json.token)
  webhook.send(('Censor Bot was down for ' + uptime[uptime.length - 1].toString() + 'seconds'))
}).catch(err => {
  console.log(err)
});
