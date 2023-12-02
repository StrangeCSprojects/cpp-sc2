import React from "react";
import "./style.css";

export const Box = () => {
  return (
    <div className="box">
      <div className="settings-page">
        <div className="group">
          <div className="div">
            <img className="img" alt="Group" src="group-6.png" />
            <img className="group-2" alt="Group" src="group-7.png" />
            <img className="group-3" alt="Group" src="group-8.png" />
            <img className="group-4" alt="Group" src="group-9.png" />
          </div>
          <div className="group-wrapper">
            <div className="group-5">
              <div className="overlap-group-wrapper">
                <div className="overlap-group">
                  <div className="text-wrapper">Your Name:</div>
                  <div className="text-wrapper-2">John Smith</div>
                  <img className="group-6" alt="Group" src="group-22.png" />
                </div>
              </div>
              <div className="overlap-wrapper">
                <div className="overlap-group">
                  <div className="text-wrapper">Your Email:</div>
                  <div className="text-wrapper-3">JohnSmith@gmail.com</div>
                  <img className="group-6" alt="Group" src="image.png" />
                </div>
              </div>
              <div className="div-wrapper">
                <div className="overlap-group">
                  <div className="text-wrapper-4">Your Password:</div>
                  <div className="text-wrapper-5">********</div>
                  <img className="group-6" alt="Group" src="group-22-2.png" />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
