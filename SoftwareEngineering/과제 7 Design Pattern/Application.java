public abstract class Application {
	
	public boolean open(String fileName) {
		// check whether the file can be read!
		if ( check(fileName) == false ) return false;

		// read and process the file		
		return process(fileName);
	}
	
	protected abstract boolean process(String fileName);
	protected abstract boolean check(String fileName);
}