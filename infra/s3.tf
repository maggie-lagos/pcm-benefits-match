resource "aws_s3_bucket" "pcm_static_test" {
  bucket  = "test-pcm-static"
  tags    = {
	Name          = "PCMStaticFiles"
	Environment    = "Test"
  }
}