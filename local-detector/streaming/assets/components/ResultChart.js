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
  const canvas = document.getElementById('resultChart');
  let ctx = canvas.getContext('2d');
  ctx.clearRect(0, 0, canvas.width, canvas.height);

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
      events: ['click'],
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
      plugins: {
        datalabels: {
          align: 'middle',
          anchor: 'middle',        
          backgroundColor: function(context) {
            return context.dataset.backgroundColor;
          },
          font: {
            size: '28'
          },
          display: function(context) {
            const index = context.dataIndex;
            const value = context.dataset.data[index];

            return Math.round(value*100) > 0;
          },
          borderRadius: 4,
          color: 'black',
          formatter: function(value, context) {
            return Math.round(value*100) + '%';
          }
        }
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
  const canvas = document.getElementById('resultChart');
  let ctx = canvas.getContext('2d');
  ctx.clearRect(0, 0, canvas.width, canvas.height);

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
      events: ['click'],
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
      },
      plugins: {
        datalabels: {
          align: 'end',
          anchor: 'end',        
          backgroundColor: function(context) {
            return context.dataset.backgroundColor;
          },
          font: {
            size: '24'
          },
          borderRadius: 4,
          color: 'black',
          formatter: function(value, context) {
            return Math.round(value) + '%';
          }
        }
      }
    }
  });
}