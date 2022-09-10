var canvas = document.querySelector('canvas');

canvas.width = 1900;
canvas.height = 950;

var c = canvas.getContext('2d');

const base_url = window.location.href;

function animate() {
    $.getJSON(base_url + '/_update_pos', function(particle_data){
        c.fillStyle = 'rgba(10,10,20,0.2)';
        c.fillRect(0, 0, 1900, 950);
        for (const [key, value] of Object.entries(particle_data)) {
            const pos_data = value.split(",");
            c.beginPath();
            c.arc(pos_data[0].slice(2), pos_data[1].slice(0, -1), 2, 0, 2 * Math.PI, false);
            c.fillStyle = `rgba(250, 250, 250, ${pos_data[2].slice(0, -1)})`;
            c.fill();
        }
    });
    // animate();
    setTimeout(() => animate(), 18);
}

c.fillStyle = 'rgba(10,10,20,1)';
c.fillRect(0, 0, 1900, 950);

animate();