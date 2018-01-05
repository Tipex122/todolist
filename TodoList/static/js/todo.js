$(function() {

    $('#suggestion').keyup(function(){
        var query;
        query = $(this).val();
        $.get('/suggest_todos/', {suggestion: query}, function(data){
            $('#cats').html(data);
/*
                $('.todo-add').click(function(){
                    //on pourrait n'utiliser que todoid OU todoname
                    //mais l'emploi de todoname peut être intéressant dans le cas d'une validation clavier
                    var todoid = $(this).attr("todo-id");
                    var todoname = $(this).attr("todo-title");

                    var me = $(this);
                    //associe le click de souris à la fonction "def auto_add_todo(request)"
                    //fonction qui rajoute le bouton "todo_id" à la <div id="lists-todos"
                    $.get('/auto_add_todo/', {todo_id: todoid, title: todoname}, function(data){
                        $('#list-todos').html(data);
                        //$('#list-todos').insertAfter('<hr>');
                        me.hide();
                    });
                        //alert( "Load was performed." );
                });
*/
                $('.todo-add').click(function(){
                    //var me = $(this);
                    //foctionnement étrange ==> c'est HR (ou #un) qui se déplace
                    $(this).before($('#un'))
                    //$('<p>Test ajout </p>').insertAfter('<hr>')
                });

        });

        //alert( "Load was performed." );
        $(this).keypress(function(e) {
            if(e.which == 13)
              $('#list-todos').text(query);  //keyCode
        });

    });

});

