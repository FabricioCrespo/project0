document.addEventListener('DOMContentLoaded', () => {

    // Connect to websocket
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    // When connected, configure buttons
    socket.on('connect', () => {

        // Each button should emit a "submit vote" event
        document.querySelectorAll('button').forEach(button => {
            button.onclick = () => {
                const individual_message = button.dataset.message; //Data set no es por la base de datos sino por el html
                socket.emit('send message', {'individual_message': individual_message});
            };
        });
    });

    // When a new vote is announced, add to the unordered list
    socket.on('messages', data => {
        const li = document.createElement('li');
        li.innerHTML = `Message sended: ${data.individual_message}`;
        document.querySelector('#messages').append(li);
    });
});
