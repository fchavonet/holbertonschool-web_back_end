import { expect } from "chai";
import kue from "kue";
import createPushNotificationsJobs from "./8-job.js";

const queue = kue.createQueue();

describe("createPushNotificationsJobs", () => {
  before(() => {
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit();
  });

  it("should display an error message if jobs is not an array", () => {
    expect(() => createPushNotificationsJobs("not-an-array", queue)).to.throw(Error, "Jobs is not an array");
  });

  it("should create two new jobs to the queue", () => {
    const mockJobs = [
      {
        phoneNumber: "4153518780",
        message: "This is the code 1234 to verify your account"
      },
      {
        phoneNumber: "4153518781",
        message: "This is the code 4562 to verify your account"
      }
    ];

    createPushNotificationsJobs(mockJobs, queue);
    expect(queue.testMode.jobs.length).to.equal(2);
  });

  it("should verify the data and job type of each job", () => {
    const mockJobs = [
      {
        phoneNumber: "4153518780",
        message: "This is the code 1234 to verify your account"
      },
      {
        phoneNumber: "4153518781",
        message: "This is the code 4562 to verify your account"
      }
    ];

    createPushNotificationsJobs(mockJobs, queue);

    queue.testMode.jobs.forEach((job, index) => {
      expect(job.type).to.equal("push_notification_code_3");
      expect(job.data).to.deep.equal(mockJobs[index]);
    });
  });
});
