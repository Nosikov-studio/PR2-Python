function createAddress(type) {
	const address = type.toUpperCase();
	return function (name) {
		return `${address} ${name}`
		
	}
}

const addresGrajdanin = createAddress ('Гражданин');
const addresGrajdanka = createAddress ('Гражданка');


console.log(addresGrajdanin('Василий'))
console.log(addresGrajdanka('Алёна'))

