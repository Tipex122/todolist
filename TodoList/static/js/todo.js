$('#suggestion').keyup(function(){
        var query;
        query = $(this).val();
        $.get('/suggest_todos/', {suggestion: query}, function(data){
            $('#cats').html(data);
        });
        //alert( "Load was performed." );
});

//Ne fonctionne pas. Sans doute que JS n'est pas chargé pour les nouveaux boutons (?)
$('#todo-add').click(function(){
    var todoid = $(this).attr("todo-id");
    //var name = $(this).text();
    var todoname = $(this).attr("todo-title");
    var me = $(this)
    $.get('/auto_add_todo/', {todo_id: todoid, title: todoname}, function(data){
        $('#list-todos').html(data);
        //me.hide();
        });
        alert( "Load was performed." );
});

