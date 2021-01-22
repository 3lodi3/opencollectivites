from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html

from core import models


class TimeStampModelAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at", "updated_at"]

    class Meta:
        abstract = True


@admin.register(models.Metadata)
class MetadataAdmin(TimeStampModelAdmin):
    pass


@admin.register(models.DataYear)
class DataYearAdmin(TimeStampModelAdmin):
    pass


@admin.register(models.Scope)
class ScopeAdmin(TimeStampModelAdmin):
    search_fields = ("name",)
    list_display = ("name", "view_sources_link")
    ordering = ["name"]

    def view_sources_link(self, obj):
        count = obj.source_set.count()
        url = (
            reverse("admin:core_source_changelist")
            + "?"
            + urlencode({"scope__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} sources</a>', url, count)

    view_sources_link.short_description = "Sources"


@admin.register(models.Document)
class DocumentAdmin(TimeStampModelAdmin):
    search_fields = ("title", "url")
    list_display = ("__str__", "is_published", "last_update", "view_rss_post_link")
    list_filter = ("is_published", "source__editor", "source")

    raw_id_fields = ("rss_post", "epcis", "communes")

    fields = (
        "title",
        "url",
        "base_domain",
        "source",
        "is_published",
        "rss_post",
        "view_rss_post_content",
        "publication_pages",
        "scope",
        "regions",
        "departements",
        "epcis",
        "communes",
        "topics",
        "document_type",
        "last_update",
        "created_at",
        "updated_at",
    )

    readonly_fields = [
        "base_domain",
        "view_rss_post_link",
        "view_rss_post_content",
        "created_at",
        "updated_at",
    ]

    def view_rss_post_link(self, obj):
        if obj.rss_post:
            url = reverse("admin:feeds_post_change", args=(obj.rss_post.pk,))
            return format_html('<a href="{}">Post</a>', url)
        else:
            return ""

    view_rss_post_link.short_description = "Lien post associé"

    def view_rss_post_content(self, obj):
        return obj.rss_post.body

    view_rss_post_content.short_description = "Contenu du post associé"


@admin.register(models.Source)
class SourceAdmin(TimeStampModelAdmin):
    search_fields = ("title", "url")
    list_display = (
        "__str__",
        "last_update",
        "view_rss_feed_link",
        "view_documents_link",
    )
    list_filter = (
        "source_type",
        "editor",
    )
    raw_id_fields = ("rss_feed", "epcis", "communes")

    readonly_fields = [
        "base_domain",
        "created_at",
        "updated_at",
    ]

    def view_rss_feed_link(self, obj):
        if obj.rss_feed:
            url = reverse("admin:feeds_source_change", args=(obj.rss_feed.pk,))
            return format_html('<a href="{}">Flux</a>', url)
        else:
            return ""

    view_rss_feed_link.short_description = "Lien flux associé"

    def view_documents_link(self, obj):
        count = obj.document_set.count()
        url = (
            reverse("admin:core_document_changelist")
            + "?"
            + urlencode({"source__id": f"{obj.pk}"})
        )
        return format_html('<a href="{}">{} documents</a>', url, count)

    view_documents_link.short_description = "Documents"


admin.site.register(models.Topic)
admin.site.register(models.Editor)
admin.site.register(models.DocumentType)
admin.site.register(models.PageType)
