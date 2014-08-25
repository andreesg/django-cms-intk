BEGIN;
DROP TABLE `aldryn_blog_authorsplugin`;
ALTER TABLE `aldryn_blog_latestentriesplugin_tags` DROP FOREIGN KEY `latestentriesplugin_id_refs_cmsplugin_ptr_id_25eb8400`;
DROP TABLE `aldryn_blog_latestentriesplugin`;
DROP TABLE `aldryn_blog_latestentriesplugin_tags`;
ALTER TABLE `aldryn_blog_post_coauthors` DROP FOREIGN KEY `post_id_refs_id_24d64ec2`;
DROP TABLE `aldryn_blog_post`;
DROP TABLE `aldryn_blog_post_coauthors`;
ALTER TABLE `aldryn_blog_category_translation` DROP FOREIGN KEY `master_id_refs_id_07d1094e`;
DROP TABLE `aldryn_blog_category`;
DROP TABLE `aldryn_blog_category_translation`;

COMMIT;
