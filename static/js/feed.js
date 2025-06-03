function Add()
{
    location.href = "/new_post";
}

function Search()
{
    location.href = "?hashtag=" + document.getElementById("search").value;
}