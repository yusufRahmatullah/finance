function fillTable(data) {
  var totalBudget = q('#budget_left');
  var walletJenius = q('#wallet_jenius');
  var total = q('#total');

  totalBudget.innerHTML = humanizeAmount(data.budget_left);
  walletJenius.innerHTML = humanizeAmount(data.wallet_jenius);
  total.innerHTML = humanizeAmount(data.total);
}

function loadSummary() {
  setPeriod();

  fetch('/summary')
  .then(resp => resp.json())
  .then(data => {
    fillTable(data);
  })
  .catch(err => {
    console.error("Failed get budgets. " + err);
  })
}
