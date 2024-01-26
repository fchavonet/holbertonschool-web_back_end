import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, filename) {
  return Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(filename)])
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
