import Loader from "react-loader-spinner";
import React, { useState } from "react";
import { sendURL } from "../actions/FlaskActions";

export const InputForm = () => {
  const [urlState, setUrlState] = useState("");
  const [loadingState, setLoadingState] = useState(false);

  const onSubmitForm = async (e: any) => {
    e.preventDefault();
    setLoadingState(true);
    await sendURL(urlState);
    setLoadingState(false);
  };

  const onChange = (e: any) => {
    setUrlState(e.target.value);
  };

  return (
    <div className="container mx-auto">
      <div className="max-w-md mx-auto">
        <form className="bg-white shadow-md rounded px-8 pt-7 pb-8 mb-4">
          <label className="block text-gray-700 text-sm font-bold mb-2">
            Вставьте URL сюда
          </label>
          <input
            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            id="username"
            type="text"
            placeholder="Вставьте URL сюда"
            value={urlState}
            onChange={(e) => onChange(e)}
          />
          <div className="flex items-center justify-between">
            <button
              className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow"
              type="button"
              onClick={onSubmitForm}
            >
              Скачать
            </button>
            {loadingState && <Loader type="ThreeDots" color="#19619d" />}
          </div>
        </form>
      </div>
    </div>
  );
};
