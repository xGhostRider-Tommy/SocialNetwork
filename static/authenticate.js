function getCookie(name)
{
    const cookies = document.cookie.split(';');
    for (let cookie of cookies)
    {
        const [key, value] = cookie.trim().split('=');
        if (key === name)
        {
            return decodeURIComponent(value);
        }
    }
    return null;
}

const localUsername = getCookie("Username")
const localSessionID = getCookie("SessionID");

window.onload = function()
{
      if (localUsername && localSessionID)
      {
            document.getElementById("localUsername").value = localUsername;
            document.getElementById("localSessionID").value = localSessionID;

            document.getElementById("AutoForm").submit();
      }
      else
      {
            window.location.href = "/login";
      }
}