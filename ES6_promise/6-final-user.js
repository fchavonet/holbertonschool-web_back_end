import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, filename) {
  const signUpPromise = signUpUser(firstName, lastName);
  const uploadPromise = uploadPhoto(filename);

  return Promise.allSettled([signUpPromise, uploadPromise])
    .then((results) => {
      const resultArray = [];
      results.forEach((result) => {
        if (result.status === 'fulfilled') {
          resultArray.push({
            status: result.status,
            value: result.value,
          });
        } else {
          resultArray.push({
            status: result.status,
            value: result.reason,
          });
        }
      });
      return resultArray;
    });
}
