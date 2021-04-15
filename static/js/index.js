function fillTable(data) {
  var totalBudget = q('#budget_left');
  var walletJenius = q('#wallet_jenius');
  var total = q('#total');

  totalBudget.innerHTML = humanizeAmount(data.budget_left);
  walletJenius.innerHTML = humanizeAmount(data.wallet_jenius);
  total.innerHTML = humanizeAmount(data.total);
}

async function loadSummary() {
  setPeriod();

  var data = await fetchApi(API.summary);
  fillTable(data);
}
