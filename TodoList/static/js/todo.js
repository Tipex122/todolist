$('#suggestion').keyup(function(){
        var query;
        query = $(this).val();
        $.get('/suggest_todos/', {suggestion: query}, function(data){
        //$.get('{% url "suggest_todos" %}', {suggestion: query}, function(data){
        $('#cats').html(data);
        });
});
