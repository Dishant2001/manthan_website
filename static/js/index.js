function hinglishtext()
{
    let text=$("#input").val();
    console.log(text);
    $.ajax({
        url:'/',
        type:'POST',
        data:{'query':text},
        success: function(response){
            console.log(response);
            let englishResponse=response['response'];
            $("#output").val(englishResponse);
        }
    })
}

function translate()
{
    hinglishtext();
}