const chai = require("chai");
const sinon = require("sinon");
const Utils = require("./utils.js");
const sendPaymentRequestToApi = require("./3-payment.js");


describe("sendPaymentRequestToApi", function () {
    const calculateNumberSpy = sinon.spy(Utils, "calculateNumber");

    it("Validate the usage of the Utils function.", () => {
        sendPaymentRequestToApi(100, 20);

        chai.expect(calculateNumberSpy.calledOnce).to.be.true;
        chai.expect(calculateNumberSpy.calledWith("SUM", 100, 20)).to.be.true;

        calculateNumberSpy.restore()
    });
});
