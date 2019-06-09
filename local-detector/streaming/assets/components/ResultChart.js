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
  var ctx = document.getElementById('resultChart').getContext('2d');
  var chart = new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: chartLabels,
      datasets: [{
        label: 'Emotion Detection Result',
        data: res,
        backgroundColor: backgroundColors,
        borderWidth: 1
      }]
    },

    // Configuration options go here
    options: {
      legend: {
        display: true,
        labels: {
          // Filter out labels with no result
          filter: function(item, data) {
            const items = data.datasets[0].data 
            const emotionIdx = data.labels.findIndex(i => i === item.text);
            return items[emotionIdx] > 0;
          }
        }
      },
      title: {
        display: true,
        text: 'Emotion Detection Result'
      },
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
    type: 'bar',
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