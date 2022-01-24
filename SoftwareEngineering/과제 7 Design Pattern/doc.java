
public class doc extends Application {

	@Override
	protected boolean process(String fileName) {
		// 주어진 file이 DOC 파일의 내용을 처리함
		return false;
	}

	@Override
	protected boolean check(String fileName) {
		// 주어진 file이 DOC의 format인지 확인함
		return false;
	}

}
