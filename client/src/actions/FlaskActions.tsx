import axios from "axios";

export const sendURL = async (YouTubeURL: any) => {
  const body = JSON.stringify(YouTubeURL);

  const config = {
    headers: {
      "Content-Type": "application/json",
    },
  };
  try {
    const response = await axios.post("/api/converter", body, config);
    const downloadFile = await getFile(response);
  } catch (err) {
    console.log("This broke lets see if i can capture");
    return false;
  }
};

export const getFile = async (response: any) => {
  const redirect = window.location.assign(`/api/getFile/${response.data}`);
};
