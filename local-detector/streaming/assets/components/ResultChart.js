const backgroundColors = [
  '#F9F871',
  '#00C0EF',
  '#00D7D8',
  '#33E9B2',
  '#A3F489',
  '#00A5ED',
  '#A4449C',
  '#AD2175',
];
const chartLabels = ['Anger', 'Contempt', 'Disgust', 'Fear', 'Happiness', 'Neutral', 'Sadness', 'Surprise'];

function initResultChart (res) {
  let ctx = document.getElementById('resultChart').getContext('2d');
  let datasets = [];
  
  for (let k = 0; k < res.length; k++) {
    datasets.push({
      label: `Emotion Detection Result #${k+1}`,
      data: res[k],
      backgroundColor: backgroundColors,
      borderWidth: 1
    })
  }

  let chart = new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: chartLabels,
      datasets: datasets
    },

    // Configuration options go here
    options: {
      legend: {
        display: true,
        labels: {
          // Filter out labels with no result
          filter: function(item, data) {
            let found = false;
            for (var i = 0; i < data.datasets.length; i++) {
              let items = data.datasets[i].data;
              const emotionIdx = data.labels.findIndex(i => i === item.text);
              if (items[emotionIdx] > 0) found = true;
            }

            return found;
          }
        }
      },
      title: {
        display: true,
        text: 'Emotion Detection Result'
      },
      cutoutPercentage: 30,
      animation: {
        animateScale: true,
        duration: 5000
      }
    }
  });
};

function getStatsChart(res) {
  var ctx = document.getElementById('resultChart').getContext('2d');
  var chart = new Chart(ctx, {
    type: 'horizontalBar',
    data: {
      labels: chartLabels,
      datasets: [{
        label: 'Average',
        data: res,
        backgroundColor: backgroundColors,
        borderWidth: 1
      }]
    },

    options: {
      legend: {
        display: false
      },
      title: {
        display: true,
        text: 'Inferences by Emotion'
      },
      animation: {
        animateScale: true,
        duration: 5000
      }
    }
  });
}