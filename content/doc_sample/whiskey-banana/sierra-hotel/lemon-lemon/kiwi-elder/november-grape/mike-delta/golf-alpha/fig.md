# Play: Fig - setup

- hosts: all
  become: true
  vars:
    app_name: "fig_app"
    retry_count: 4

  tasks:
    - name: Ensure romeo-task-1 is present
      ansible.builtin.file:
        path: /opt/fig/romeo-task-1
        state: directory

    - name: Template romeo-task-1 config
      ansible.builtin.template:
        src: templates/romeo-task-1.j2
        dest: /etc/fig/romeo-task-1.conf
        mode: '0644'

    # Description:
    # Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

  handlers:
    - name: restart fig service
      ansible.builtin.service:
        name: fig
        state: restarted

## Notes

Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. 

***
Generated: 2025-11-07T18:27:44Z
