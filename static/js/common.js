const MONTH = ['',
  'Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'jun',
  'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Des'
];

function appendNode(node, html) {
  node.insertAdjacentHTML('beforeend', html);
}

function getPeriod() {
  var d = new(Date);
  var year = d.getFullYear();
  var month = d.getMonth() + 1;
  var day = d.getDate();
  if (day >= 27) {
    month++;
    if (month >= 12) {
      year++;
      month = 1
    }
  }
  return [year, month]
}

function humanizeAmount(amount) {
  if (!amount || amount == 0) {
    return '-';
  }
  return 'Rp' + amount.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
}

function humanizeName(name) {
  if (!name) {
    return "";
  }

  var tokens = name.split('_');
  var res = [];

  tokens.forEach(token => {
    var title = token[0].toUpperCase() + token.substr(1);
    res.push(title);
  });

  return res.join(' ')
}

function humanizePeriod(period) {
  var year = period[0];
  var month = period[1];

  return `${MONTH[month]} ${year}`;
}

function q(query) {
  return document.querySelector(query);
}

function setPeriod() {
  var period = getPeriod();
  var node = q('#selected-menu');

  node.innerHTML += ` - ${humanizePeriod(period)}`;
}

function showForm() {
  var form = q('form');
  form.style.display = "block";
}

function showTable() {
  var progressBar = q('#progress-bar');
  var tableNode = q('table');

  progressBar.style.visibility = "hidden";
  tableNode.style.visibility = "visible";
}
