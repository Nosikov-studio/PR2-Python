function external () {
	
	const externalVar ="я внешняя функция";
	
	function internal() {
		const internalVar ="я внутренняя функция";
			console.log('internalVar>',internalVar );
			console.log('externalVar>',externalVar );
		
	}
	return internal
}

const intrnalFn = external()

intrnalFn()