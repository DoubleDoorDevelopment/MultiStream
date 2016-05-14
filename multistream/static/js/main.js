$(document).ready(function(){

    // Get streams from server.
    getStreams().done(redirectUser);

    function getStreams(){
        return $.ajax({
            url: '/api_v1/streams',
            contentType: "application/json",
            type: 'GET'
        });
    }

    function redirectUser(response){
        streams = response['streams'];
        if (streams.length == 0) {
            console.log('No streams');
        } else {
        new_url = 'http://multistre.am/';

        $(streams).each(function(index, value){
            new_url += value + '/';
        });
        console.log(new_url);
        window.location.href = new_url;
        }
    }

});
