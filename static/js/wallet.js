function generateTable(wallets) {
  var tableNode = q('#table-body');
  var ctn = '';
  var total = 0;
  var total_left = 0;

  wallets.forEach(wallet => {
    ctn += walletView(wallet);
    total += wallet.amount;
    total_left += wallet.left;
  });

  ctn += walletView({
    name: 'Total',
    amount: total,
    left: total_left,
  }, true);

  appendNode(tableNode, ctn);
}

async function getWallets() {
  setPeriod();

  var data = await fetchApi(API.wallet.get);
  generateTable(data);

  showTable();
}

function walletView(wallet, bold) {
  var tr_attr = '';
  if (bold) {
    tr_attr = 'class="bold"';
  }

  return `
  <tr ${tr_attr}>
    <td>${humanizeName(wallet.name)}</td>
    <td>${humanizeAmount(wallet.left)}</td>
  </tr>
  `;
}
