import kue from "kue";

const queue = kue.createQueue();

const jobData = {
	phoneNumber: "4153518780",
	message: "This is a test notification",
};

const job = queue
	.create("push_notification_code", jobData)
	.save((error) => {
		if (error) {
			console.error("Failed to create notification job: " + error.message);
			return;
		}
		console.log("Notification job created:", job.id);
	});

job.on("complete", () => {
	console.log("Notification job completed");
});

job.on("failed", () => {
	console.log("Notification job failed");
});